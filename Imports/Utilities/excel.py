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
	# TODO ACCOUNTED verify sheet formatting here based on fileType
	return sheet


def processQuickBooksReport(filePath):
	return {} # TODO ACCOUNTED


def processAmazonReport(filePath, quickBooksRecords):
	workBook = loadWorkbook(AMAZON, filePath, False)
	sheet = loadSheet(workBook, AMAZON)

	orders = {}
	nonOrders = []

	for i in range(8 + 1, sheet.max_row + 1): # TODO store start value in constant
		recordType = readCellString(sheet, i, 3) # TODO store column index in constant
		if recordType == 'ORDER': #TODO constant
			pass # TODO ACCOUNTED store in orders
		else:
			nonOrders.append(AmazonNonOrderRecord(i, readCellDateString(sheet, i, 1), recordType))
	
	for i in nonOrders:
		print(i.summarize())

def readCellString(sheet, row, column):
	return str(sheet.cell(row = row, column = column).value).upper()

def readCellDateString(sheet, row, column):
	dateString = readCellString(sheet, row, column)
	return datetime.strptime(dateString[0 : dateString.index(',') + 6], '%b %d, %Y')
