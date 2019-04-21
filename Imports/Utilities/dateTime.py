import datetime

def getDateTime():
	return datetime.datetime.now()

def getDateTimeAsFilePathSegment():
	return getDateTime().strftime('%Y_%m_%d_%H%M')

def subtractDay(date1, date2):
	return (date1 - date2).days