from .fileManagement import *
from .output import *

def processReports():
	filePaths = collectFilePaths()

	summaryData = collectSummaryData()
	# beginningBalanceSubtotal = promptForManualDataEntry('Beginning Balance Subtotal')
	# ordersSubtotal = promptForManualDataEntry('Orders Subtotal')
	# refundsSubtotal = promptForManualDataEntry('Refunds Subtotal')
	# shippingServicesSubtotal = promptForManualDataEntry('Shipping Services Subtotal')
	# totalBalance = promptForManualDataEntry('Total Balance')
	# unavailableBalance = promptForManualDataEntry('Unavailable Balance')
	# transferAmount = promptForManualDataEntry('Transfer Amount')

	print(filePaths)
	print(summaryData)


def collectFilePaths():
	filePaths = {}
	filePaths['Amazon'] = promptForFilePath('Amazon')
	filePaths['QuickBooks'] = promptForFilePath('QuickBooks')
	return filePaths


def collectSummaryData():
	output('Please enter the following values from the Amazon summary:')
	summaryData = {}
	summaryData['Beginning Balance Subtotal'] = float(prompt('Beginning Balance Subtotal','$').replace(',',''))
	return summaryData