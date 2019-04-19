import os

def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')


def output(text):
	print(text)


def prompt(text = '', prefix = ''):
	return input(text + ' > ' + prefix).upper()