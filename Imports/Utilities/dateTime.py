import datetime

def getDateTime():
	return datetime.datetime.now()

def getDateTimeAsFilePathSegment():
	return getDateTime().strftime('%Y_%m_%d_%H%M')