from .constants import *
from .fileManagement import *
from .output import *

def processReports():
	filePaths = collectFilePaths()
	amazonSummaryData = collectAmazonSummaryData()


def collectFilePaths():
	filePaths = {}
	for fileType in FILE_TYPES:
		filePaths[fileType] = promptForFilePath(fileType)
	return filePaths


def collectAmazonSummaryData():
	output('Please enter the following values from the Amazon summary:')
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