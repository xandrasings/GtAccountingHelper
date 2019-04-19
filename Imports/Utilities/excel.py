from .constants import *
from .fileManagement import *
from ..Classes.AmazonNonOrderRecord import *
from ..Classes.AmazonOrderRecord import *
from ..Classes.CutOffSplit import *
from ..Classes.QuickBooksRecord import *

from datetime import datetime
from openpyxl import load_workbook


def loadWorkbook(fileType, filePath, readOnly = False):
	try:
		return load_workbook(filePath, readOnly)
	except:
		quit('Could not open workbook for ' + fileType + '.')


def loadSheet(workbook, fileType):
	sheet = None
	if SHEET not in LOCATION[fileType] or len(workbook.sheetnames) == 1:
		try:
			sheet = workbook.get_active_sheet()
		except:
			quit('Could not open active sheet of ' + fileType + ' workbook.')
	else:
		sheetName = LOCATION[fileType][SHEET]
		try:
			sheet = workbook[sheetName]
		except:
			quit('Could not open sheet ' + sheetName + ' of ' + fileType + ' workbook.')

	verifySheetFormatting(fileType, sheet)
	return sheet

def verifySheetFormatting(fileType, sheet):
	verifyColumnMax(fileType, sheet)
	verifyHeaderContent(fileType, sheet)

def verifyColumnMax(fileType, sheet):
	actualColumnMax = sheet.max_column
	expectedColumnMax = LOCATION[fileType][COLUMN][MAX]
	if actualColumnMax != expectedColumnMax:
		quit(fileType + ' workbook had ' + str(actualColumnMax) + ' column max instead of expected value ' + str(expectedColumnMax) + '.')

def verifyHeaderContent(fileType, sheet):
	row = LOCATION[fileType][ROW][HEADER]
	for column, expectedContent in LOCATION[fileType][HEADER].items():
		if getCellString(sheet, row, column) != expectedContent.upper():
			quit(fileType + ' workbook did not have expected column header ' + expectedContent + ' in row ' + str(row) + ' column ' + str(column) + '.')


def setCellValue(sheet, row, column, value):
	sheet.cell(row = row, column = column).value = value;


def getCellValue(sheet, row, column):
	try:
		return sheet.cell(row = row, column = column).value
	except:
		quit('Could not get cell value for row ' + str(row) + ', column ' + str(column) + '.')


def getCellString(sheet, row, column):
	cellValue = getCellValue(sheet, row, column)
	try:
		return str(cellValue).upper().strip()
	except:
		quit('Could not convert cell value for row ' + str(row) + ', column ' + str(column) + ' to string.')


def getCellFloat(sheet, row, column):
	cellValue = getCellValue(sheet, row, column)
	try:
		if cellValue == None:
			cellValue = 0
		return float(cellValue)
	except:
		quit('Could not convert cell value ' + cellValue + ' to float.')


def getCellDateString(fileType, sheet, row, column):
	dateString = getCellString(sheet, row, column)
	try:
		return datetime.strptime(dateString[0 : dateString.index(',') + 6], '%b %d, %Y')
	except:
		quit('Could not convert date string ' + dateString + ' to datetime.')


def processQuickBooksReport(filePath):
	workbook = loadWorkbook(QUICKBOOKS, filePath, True)
	sheet = loadSheet(workbook, QUICKBOOKS)

	invoices = []

	for row in range(LOCATION[QUICKBOOKS][ROW][HEADER] + 1, sheet.max_row + 1):
		date = getCellValue(sheet, row, LOCATION[QUICKBOOKS][COLUMN][DATE])
		invoiceNumber = getCellString(sheet, row, LOCATION[QUICKBOOKS][COLUMN][INVOICE_NUMBER])
		city = getCellString(sheet, row, LOCATION[QUICKBOOKS][COLUMN][CITY])
		debit = getCellFloat(sheet, row, LOCATION[QUICKBOOKS][COLUMN][DEBIT])
		credit = getCellFloat(sheet, row, LOCATION[QUICKBOOKS][COLUMN][CREDIT])

		invoices.append(QuickBooksRecord(date, invoiceNumber, city, debit, credit))

	return invoices


def processAmazonReport(amazonFilePath, quickBooksRecords, unavailableBalance, reportFilePath):
	workbook = loadWorkbook(AMAZON, amazonFilePath, False)
	sheet = loadSheet(workbook, AMAZON)

	orders = []
	nonOrders = []

	for row in range(LOCATION[AMAZON][ROW][HEADER] + 1, sheet.max_row + 1):
		recordType = getCellString(sheet, row, LOCATION[AMAZON][COLUMN][TYPE]) 
		date = getCellDateString(AMAZON, sheet, row, LOCATION[AMAZON][COLUMN][DATE])

		if recordType == ORDER:
			city = getCellString(sheet, row, LOCATION[AMAZON][COLUMN][CITY])
			orderId = getCellString(sheet, row, LOCATION[AMAZON][COLUMN][ORDER_ID])
			productSales = getCellFloat(sheet, row, LOCATION[AMAZON][COLUMN][PRODUCT_SALES])
			shippingCredits = getCellFloat(sheet, row, LOCATION[AMAZON][COLUMN][SHIPPING_CREDITS])
			salesTaxCollected = getCellFloat(sheet, row, LOCATION[AMAZON][COLUMN][SALES_TAX_COLLECTED])
			sellingFees = getCellFloat(sheet, row, LOCATION[AMAZON][COLUMN][SELLING_FEES])
			total = getCellFloat(sheet, row, LOCATION[AMAZON][COLUMN][TOTAL])
			orders.append(AmazonOrderRecord(row, date, orderId, city, productSales, shippingCredits, salesTaxCollected, sellingFees, total))
		else:
			nonOrders.append(AmazonNonOrderRecord(row, date, recordType))
	
	populateInvoiceNumbers(orders, quickBooksRecords)
	cutOffSplit = identifyCutOffRecords(orders, unavailableBalance)

	modifyAmazonReport(sheet, orders, nonOrders)
	saveAmazonReport(workbook, reportFilePath)
	workbook.save(reportFilePath)

def populateInvoiceNumbers(orders, quickBooksRecords):
	pass # TADA populate invoice number #WRITE_LOGIC_FOR_MATCHING_TRANSACTIONS


def identifyCutOffRecords(orders, unavailableBalance):
	pass # TADA identify cut off records #WRITE_LOGIC_FOR_CUTOFF
	# TADA if able to sort out the cut off records, turn them True and return none
	# TADA else sum array values from bottom up until value is above unavailable balance, set them to cutoffTrue
	# TADA mark row and calculate cutoff, return as CutOffSplit


def saveAmazonReport(workbook, filePath):
	workbook.save(filePath)
	clearScreen()
	output('Report saved to ' + filePath)


def modifyAmazonReport(sheet, orders, nonOrders):
	markCutOffRecords(sheet, orders)
	addNewDataColumns(sheet, orders)
	copyNonOrders(sheet, nonOrders)
	removeNonOrders(sheet, nonOrders)
	removeHeaderRows(sheet)


def markCutOffRecords(sheet, orders):
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
	for order in orders:
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

