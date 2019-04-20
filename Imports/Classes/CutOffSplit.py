class CutOffSplit:
	def __init__(self, row, taxedTotal, unavailableBalance):
		self.row = row
		self.taxedTotal = taxedTotal
		self.unavailableBalance = unavailableBalance

	def getRow(self):
		return self.row

	def getTaxedTotal(self):
		return self.taxedTotal

	def getUnavailableBalance(self):
		return self.unavailableBalance

	def summarize(self):
		return "{row: " + str(self.row) + ", taxed total: " + str(self.taxedTotal)  + ", unavailable balance: " + str(self.unavailableBalance) + "}"