from .constants import *
from .fileManagement import *
from ..Classes.AmazonNonOrderRecord import *
from ..Classes.AmazonOrderRecord import *

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
		date = getCellDateString(sheet, row, LOCATION[AMAZON][COLUMN][DATE])
		if recordType == ORDER:
			city = getCellString(sheet, row, LOCATION[AMAZON][COLUMN][CITY])
			orderId = getCellString(sheet, row, LOCATION[AMAZON][COLUMN][ORDER_ID])
			if city not in orders:
				orders[city] = {}
			if orderId not in orders[city]:
				orders[city][orderId] = []
			orders[city][orderId].append(AmazonOrderRecord(row, date, '')) # TADA populate cash received 
		else:
			nonOrders.append(AmazonNonOrderRecord(row, date, recordType))

	# populate invoice number

	modifyAmazonReport(sheet, orders, nonOrders)
	workBook.save('happylilfile.xlsx') # TADA


def modifyAmazonReport(sheet, orders, nonOrders):
	addNewDataColumns(sheet, orders)
	copyNonOrders(sheet, nonOrders)
	removeNonOrders(sheet, nonOrders)
	removeHeaderRows(sheet)


def addNewDataColumns(sheet, orders):
	addHeaders(sheet)
	addNewData(sheet, orders)


def addHeaders(sheet):
	for header in [CASH_RECEIVED, INVOICE]:
		addHeader(sheet, header)


def addHeader(sheet, header):
	setCellValue(sheet, LOCATION[AMAZON][ROW][HEADER], LOCATION[AMAZON][COLUMN][header], header)


def addNewData(sheet, orders):
	for ordersByCity in orders.values():
		for ordersByInvoice in ordersByCity.values():
			for order in ordersByInvoice:
				setCellValue(sheet, order.getRow(), LOCATION[AMAZON][COLUMN][CASH_RECEIVED], order.getCashReceived())
				setCellValue(sheet, order.getRow(), LOCATION[AMAZON][COLUMN][INVOICE], order.getInvoice())


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

