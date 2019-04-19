from .constants import *
from .fileManagement import *
from .output import *

def processReports():
	filePaths = collectFilePaths()
	amazonSummaryData = collectAmazonSummaryData()


def collectFilePaths():
	filePaths = {}
	filePaths['Amazon'] = promptForFilePath('Amazon')
	filePaths['QuickBooks'] = promptForFilePath('QuickBooks')
	return filePaths


def collectAmazonSummaryData():
	output('Please enter the following values from the Amazon summary:')
	amazonSummaryData = {}
	for i in AMAZON_SUMMARY_DATA_TYPES:
		amazonSummaryData[i] = float(prompt(i,'$').replace(',',''))
	return amazonSummaryData