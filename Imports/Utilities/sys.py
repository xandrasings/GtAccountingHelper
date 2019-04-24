import sys
from .output import *

def quit(text = ''):
	clearScreen()
	if text != '':
		output(text)
	output('Exiting the Accounting Helper!')
	prompt('Press enter to exit.')
	sys.exit()