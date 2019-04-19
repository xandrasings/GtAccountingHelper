class AmazonRecord:
	def __init__(self, row, date):
		self.row = row
		self.date = date

	def getRow(self):
		return self.row

	def getDate(self):
		return self.date

	def summarize(self):
		return "{row: " + str(self.row) + ", date: " + str(self.date) + "}"