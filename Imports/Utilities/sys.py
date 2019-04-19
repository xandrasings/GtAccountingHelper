import sys
from .output import *

def quit(text = ''):
	clearScreen()
	if text != '':
		output(text)
	output('Exiting the Accounting Helper!')
	sys.exit()