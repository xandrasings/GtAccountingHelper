from .constants import *
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
	output('Please navigate to the ' + inputType + ' report.')
	output()
	output('Searching: ' + targetDirectoryPath) # give the user path context
	validOptions = getValidPathOptions(targetDirectoryPath) # get every dir and excel file
	optionName = getOptionName(validOptions) # let user pick dir or excel file
	optionPath = extendPath(targetDirectoryPath, optionName) # extend the target path
	if isValidDirectory(optionName): # if it's a directory, recurse
		return promptForFilePath(inputType, optionPath)
	else: # otherwise, excel file is selected.
		return optionPath


def getMainPath():
	return getRealPath(os.path.dirname(sys.executable) if (hasattr(sys, FROZEN) or imp.is_frozen(MAIN)) else os.path.dirname(sys.argv[0]))


def getRealPath(path):
	return os.path.realpath(path)


def getValidPathOptions(targetDirectoryPath):
	pathContent = listdir(targetDirectoryPath)
	validOptions = filterPathOptions(pathContent)

	if len(validOptions) == 0:
		output('No valid excel files found here!')

	return validOptions


def filterPathOptions(pathContent):
	validOptions = []

	for item in list(pathContent):
		if (isValidDirectory(item) or isValidExcelFile(item)):
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
	if extension == 'back':
		return os.path.dirname(filePath)
	else:
		return os.path.join(filePath, extension)

