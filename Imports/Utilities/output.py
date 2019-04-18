import os

def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')


def output(text):
	print(text)


def prompt(text = '', default = ''):
	result = ''
	if default == '':
		result = input(text + ' > ').upper()
	else:
		outputPrompt(text)
		result = input('enter \'Y\' for \'' + default + '\' > ').upper()
		if result == 'Y':
			result = default
	return result