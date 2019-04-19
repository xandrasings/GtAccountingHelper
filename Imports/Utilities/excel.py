from .constants import *
from .fileManagement import *
from ..Classes.AmazonNonOrderRecord import *

from datetime import datetime
from openpyxl import load_workbook


def loadWorkbook(fileType, filePath, readOnly = False):
	workBook = load_workbook(filePath, readOnly)
	return workBook


def loadSheet(workBook, fileType):
	sheet = workBook.get_active_sheet()
	# TADA verify sheet formatting here based on fileType
	return sheet


def setCellValue(sheet, row, column, value):
	sheet.cell(row = row, column = column).value = value;


def getCellValue(sheet, row, column):
	return sheet.cell(row = row, column = column).value


def getCellString(sheet, row, column):
	return str(getCellValue(sheet, row, column)).upper()


def getCellDateString(sheet, row, column):
	dateString = getCellString(sheet, row, column)
	return datetime.strptime(dateString[0 : dateString.index(',') + 6], '%b %d, %Y')


def processQuickBooksReport(filePath):
	return {} # TADA


def processAmazonReport(filePath, quickBooksRecords):
	workBook = loadWorkbook(AMAZON, filePath, False)
	sheet = loadSheet(workBook, AMAZON)

	orders = {}
	nonOrders = []

	for row in range(LOCATION[AMAZON][ROW][HEADER] + 1, sheet.max_row + 1):
		recordType = getCellString(sheet, row, LOCATION[AMAZON][COLUMN][TYPE]) 
		if recordType == ORDER:
			pass # TADA ACCOUNTED store in orders
		else:
			nonOrders.append(AmazonNonOrderRecord(row, getCellDateString(sheet, row, LOCATION[AMAZON][COLUMN][DATE]), recordType))

	modifyAmazonReport(sheet, orders, nonOrders)
	workBook.save('happylilfile.xlsx') # TADA


def modifyAmazonReport(sheet, orders, nonOrders):
	copyNonOrders(sheet, nonOrders)
	removeNonOrders(sheet, nonOrders)
	removeHeaderRows(sheet)


def copyNonOrders(sheet, nonOrders):
	row = sheet.max_row + LOCATION[AMAZON][ROW][NON_ORDER_BUFFER]
	for nonOrder in sorted(nonOrders):
		for column in range(1, LOCATION[AMAZON][COLUMN][MAX] + 1):
			setCellValue(sheet, row, column, getCellValue(sheet, nonOrder.getRow(), column))
		row = row + 1
		

def removeNonOrders(sheet, nonOrders):
	for nonOrder in sorted(nonOrders, key = lambda x: x.row, reverse = True):
		sheet.delete_rows(nonOrder.row)


def removeHeaderRows(sheet):
	sheet.delete_rows(1, 7)

