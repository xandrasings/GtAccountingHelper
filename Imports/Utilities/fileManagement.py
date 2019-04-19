from .constants import *
from .dateTime import *
from .output import *
from .sys import *

from os import listdir

import imp
import os
import sys


def promptForFilePath(inputType, targetDirectoryPath = ''): 
	if targetDirectoryPath == '': # the first run of this function.
		targetDirectoryPath = getMainPath() # set the path to the main or exe path
	
	clearScreen()
	output('Please navigate to the desired ' + inputType + ' location.')
	output()
	output('Searching: ' + targetDirectoryPath) # give the user path context
	validOptions = getValidPathOptions(inputType, targetDirectoryPath) # get every valid dir and excel file 
	optionName = getOptionName(validOptions) # let user pick dir or excel file
	if optionName == CURRENT_DIRECTORY: # current directory selected, escape
		return targetDirectoryPath
	optionPath = extendPath(targetDirectoryPath, optionName) # extend the target path
	if isValidDirectory(optionName): # if it's a directory (not the current dir) recurse
		return promptForFilePath(inputType, optionPath)
	else: # otherwise we've selected an excel file
		return optionPath


def getMainPath():
	return getRealPath(os.path.dirname(sys.executable) if (hasattr(sys, FROZEN) or imp.is_frozen(MAIN)) else os.path.dirname(sys.argv[0]))


def getRealPath(path):
	return os.path.realpath(path)


def getValidPathOptions(inputType, targetDirectoryPath):
	pathContent = listdir(targetDirectoryPath)
	validOptions = filterPathOptions(inputType, pathContent)

	if len(validOptions) == 0:
		output('No valid excel files found here!')

	return validOptions


def filterPathOptions(inputType, pathContent):
	validOptions = []

	if ACCEPTS[inputType][SELF]:
		validOptions.append(CURRENT_DIRECTORY)

	for item in list(pathContent):
		if (
			(ACCEPTS[inputType][DIRECTORY] and isValidDirectory(item)) or
			(ACCEPTS[inputType][EXCEL] and isValidExcelFile(item))
		):
			validOptions.append(item)

	return validOptions


def isValidDirectory(item):
	return item == BACK or '.' not in item # must be a dir


def isValidExcelFile(item):
	status = (
		(
			item.endswith('.xlsx') or
			item.endswith('.xls')
		) and (	
			not item.startswith('~') # ignore temp files!
		)
	)
	return status


def getOptionName(validOptions):
	optionIndex = solicitPathOptionIndex(validOptions)
	if optionIndex == -1:
		return BACK
	else:
		return validOptions[optionIndex]


def solicitPathOptionIndex(validOptions):
	printPathOptions(validOptions)
	return getPathIndex(validOptions)


def printPathOptions(validOptions):
	i = 1
	for item in list(validOptions):
		output('- (' + str(i) + ') ' + item)
		i = i + 1
	output('- (B)ack')
	output('- (Q)uit')


def getPathIndex(validOptions):
	fileIndex = -2
	maxInput = len(validOptions)

	while fileIndex < -1:
		inputIndex = prompt()
		try:
			if inputIndex == 'Q':
				quit()
			elif inputIndex == 'B':
				fileIndex = -1
			else:
				fileIndex = int(inputIndex) - 1
				if fileIndex < -1 or fileIndex >= maxInput:
					output('Selection should be between 1 and ' + str(maxInput) + '.')
					fileIndex = -2
		except ValueError:
			output('Selection should be an integer.')

	return fileIndex


def extendPath(filePath, extension):
	if extension == BACK:
		return os.path.dirname(filePath)
	else:
		return os.path.join(filePath, extension)


def modifyFileName(reportFilePath, amazonFilePath):
	return extendPath(reportFilePath, os.path.splitext(os.path.basename(amazonFilePath))[0] + FILE_NAME_MODIFIER + getDateTimeAsFilePathSegment() + FILE_NAME_SUFFIX)


