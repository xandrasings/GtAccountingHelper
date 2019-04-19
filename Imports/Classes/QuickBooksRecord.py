class QuickBooksRecord:
	def __init__(self, date, invoiceNumber, debit, credit):
		self.date = date
		self.invoiceNumber = invoiceNumber
		self.total = debit - credit

	def getDate(self):
		return self.date

	def getInvoiceNumber(self):
		return self.invoiceNumber

	def getTotal(self):
		return self.total 

	def summarize(self):
		return "{date: " + str(self.date) + ", invoice number: " + self.invoiceNumber + ", total: " + str(self.total) + "}"