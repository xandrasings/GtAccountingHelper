class AmazonRecord:
	def __init__(self, date, invoice, total):
		self.date = date
		self.invoice = invoice
		self.total = total

	def getDate(self):
		return self.date

	def getInvoice(self):
		return self.invoice

	def getTotal(self):
		return self.total

	def summarize(self):
		return "{date: " + str(self.date) + ", invoice: " + self.invoice + ", total: " + str(self.total) + "}"