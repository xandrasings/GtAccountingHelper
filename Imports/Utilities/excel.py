from .constants import *
from .fileManagement import *
from ..Classes.AmazonNonOrderRecord import *
from ..Classes.AmazonOrderRecord import *
from ..Classes.QuickBooksRecord import *

from datetime import datetime
from openpyxl import load_workbook


def loadWorkbook(fileType, filePath, readOnly = False):
	workBook = load_workbook(filePath, readOnly)
	return workBook


def loadSheet(workBook, fileType):
	sheet = workBook.get_active_sheet() # TADA sheet1
	# TADA verify sheet formatting here based on fileType #READ_AMAZON_FILE #READ_QUICKBOOKS_FILE
	return sheet


def setCellValue(sheet, row, column, value):
	sheet.cell(row = row, column = column).value = value;


def getCellValue(sheet, row, column):
	return sheet.cell(row = row, column = column).value


def getCellString(sheet, row, column):
	return str(getCellValue(sheet, row, column)).upper().strip()


def getCellFloat(sheet, row, column):
	value = getCellValue(sheet, row, column)
	if value == None:
		value = 0
	return float(value)


def getCellDateString(fileType, sheet, row, column):
	dateString = getCellString(sheet, row, column)
	return datetime.strptime(dateString[0 : dateString.index(',') + 6], '%b %d, %Y')


def processQuickBooksReport(filePath):
	workBook = loadWorkbook(QUICKBOOKS, filePath, True)
	sheet = loadSheet(workBook, QUICKBOOKS)

	invoices = []

	for row in range(LOCATION[QUICKBOOKS][ROW][HEADER] + 1, sheet.max_row + 1):
		date = getCellValue(sheet, row, LOCATION[QUICKBOOKS][COLUMN][DATE])
		invoiceNumber = getCellString(sheet, row, LOCATION[QUICKBOOKS][COLUMN][INVOICE_NUMBER])
		city = getCellString(sheet, row, LOCATION[QUICKBOOKS][COLUMN][CITY])
		debit = getCellFloat(sheet, row, LOCATION[QUICKBOOKS][COLUMN][DEBIT])
		credit = getCellFloat(sheet, row, LOCATION[QUICKBOOKS][COLUMN][CREDIT])

		invoices.append(QuickBooksRecord(date, invoiceNumber, city, debit, credit))

	return invoices


def processAmazonReport(amazonFilePath, quickBooksRecords, reportFilePath):
	workBook = loadWorkbook(AMAZON, amazonFilePath, False)
	sheet = loadSheet(workBook, AMAZON)

	orders = {}
	nonOrders = []

	for row in range(LOCATION[AMAZON][ROW][HEADER] + 1, sheet.max_row + 1):
		recordType = getCellString(sheet, row, LOCATION[AMAZON][COLUMN][TYPE]) 
		date = getCellDateString(AMAZON, sheet, row, LOCATION[AMAZON][COLUMN][DATE])

		if recordType == ORDER:
			city = getCellString(sheet, row, LOCATION[AMAZON][COLUMN][CITY])
			orderId = getCellString(sheet, row, LOCATION[AMAZON][COLUMN][ORDER_ID])

			if city not in orders:
				orders[city] = {}

			if orderId not in orders[city]:
				orders[city][orderId] = []

			orders[city][orderId].append(AmazonOrderRecord(row, date, '')) # TADA populate cash received #READ_AMAZON_FILE
			# TADA populate any other math necessary for cutoff and other business logic #READ_AMAZON_FILE

		else:
			nonOrders.append(AmazonNonOrderRecord(row, date, recordType))
	
	orders = populateInvoiceNumbers(orders, quickBooksRecords)
	orders = identifyCutOffRecords(orders) # TADA include whatever manual input values are needed #WRITE_LOGIC_FOR_CUTOFF

	modifyAmazonReport(sheet, orders, nonOrders)
	workBook.save(reportFilePath)


def populateInvoiceNumbers(orders, quickBooksRecords):
	return orders # TADA populate invoice number #WRITE_LOGIC_FOR_MATCHING_TRANSACTIONS


def identifyCutOffRecords(orders):
	return orders # TADA identify cut off records #WRITE_LOGIC_FOR_CUTOFF


def modifyAmazonReport(sheet, orders, nonOrders):
	colorCutOffRecords(sheet, orders)
	addNewDataColumns(sheet, orders)
	copyNonOrders(sheet, nonOrders)
	removeNonOrders(sheet, nonOrders)
	removeHeaderRows(sheet)


def colorCutOffRecords(sheet, orders):
	pass # TADA color the records where cutOff = true #MARK_CUT_OFF_RECORDS


def addNewDataColumns(sheet, orders):
	addHeaders(sheet)
	addNewData(sheet, orders)


def addHeaders(sheet):
	for header in [INVOICE_NUMBER, CASH_RECEIVED]:
		addHeader(sheet, header)


def addHeader(sheet, header):
	setCellValue(sheet, LOCATION[AMAZON][ROW][HEADER], LOCATION[AMAZON][COLUMN][header], header)


def addNewData(sheet, orders):
	for ordersByCity in orders.values():
		for ordersByInvoiceNumber in ordersByCity.values():
			for order in ordersByInvoiceNumber:
				setCellValue(sheet, order.getRow(), LOCATION[AMAZON][COLUMN][CASH_RECEIVED], order.getCashReceived())
				setCellValue(sheet, order.getRow(), LOCATION[AMAZON][COLUMN][INVOICE_NUMBER], order.getInvoiceNumber())


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

