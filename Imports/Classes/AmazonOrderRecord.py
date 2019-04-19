from .AmazonRecord import *

class AmazonOrderRecord(AmazonRecord):
	def __init__(self, row, date):
		super().__init__(row, date)

	def summarize(self):
		return "{row: " + str(self.row) + ", date: " + str(self.date) + "}"