from .AmazonRecord import *

class AmazonNonOrderRecord(AmazonRecord):
	def __init__(self, row, date, type):
		super().__init__(row, date)
		self.type = type

	def __eq__(self, other):
		return self.date == other.date and self.type == other.type

	def __lt__(self, other):
		if self.type == other.type:
			return self.date < other.date
		else:
			return self.type < other.type

	def getType(self):
		return self.type

	def summarize(self):
		return "{row: " + str(self.row) + ", date: " + str(self.date) + ", type: " + self.type + "}"