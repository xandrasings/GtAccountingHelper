from .constants import *
from .excel import *
from .fileManagement import *
from .output import *
from .sys import *

def processReports():
	filePaths = collectFilePaths()
	amazonSummaryData = collectAmazonSummaryData()
	summarizeUserInput(filePaths, amazonSummaryData)
	quickBooksRecords = processQuickBooksReport(filePaths[QUICKBOOKS])
	filePaths[REPORT] = modifyFileName(filePaths[REPORT], filePaths[AMAZON])
	processAmazonReport(filePaths[AMAZON], quickBooksRecords, amazonSummaryData[UNAVAILABLE_BALANCE], filePaths[REPORT]);


def collectFilePaths():
	filePaths = {}
	for fileType in FILE_TYPES:
		filePaths[fileType] = promptForFilePath(fileType)
	return filePaths


def collectAmazonSummaryData():
	output('Please enter the following values from the Amazon summary:')
	output('(Press \'Q\' to quit.)')
	output()
	amazonSummaryData = {}
	for dataType in AMAZON_SUMMARY_DATA_TYPES:
		amazonSummaryData[dataType] = getNumericDataValue(dataType)
	return amazonSummaryData


def getNumericDataValue(dataType):
	while True:
		inputValue = prompt(dataType,'$')
		try:
			if inputValue == 'Q':
				quit()
			else:
				return float(inputValue.replace(',',''))
		except ValueError:
			output('Input should be a number with no letters or symbols.')


def summarizeUserInput(filePaths, amazonSummaryData):
	clearScreen()
	summarizeFilePaths(filePaths)
	summarizeAmazonSummaryData(amazonSummaryData)
	promptContinue()

def summarizeFilePaths(filePaths):
	for fileType in FILE_TYPES:
		output(fileType + ' file location: ' + filePaths[fileType])
	output()

def summarizeAmazonSummaryData(amazonSummaryData):
	for dataType in AMAZON_SUMMARY_DATA_TYPES:
		output(dataType + ' value: $' + str(amazonSummaryData[dataType]))
	output()

def promptContinue():
	output('Press enter to continue or \'Q\' to quit.')
	if prompt() == 'Q':
		quit()
