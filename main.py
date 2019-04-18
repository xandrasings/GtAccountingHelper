from Imports.Utilities.dataProcessing import *
from Imports.Utilities.output import *

def main():
	clearScreen()
	output('Welcome to Glacier Tek\'s Amazon Accounting Helper.')
	prompt('Press enter to start!')
	processInputFile('Amazon')
	clearScreen()
	processInputFile('QuickBooks')


main()