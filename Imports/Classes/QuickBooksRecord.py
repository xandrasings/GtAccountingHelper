class QuickBooksRecord:
	def __init__(self, date, invoiceNumber, city, debit, credit):
		self.date = date
		self.invoiceNumber = invoiceNumber
		self.city = city
		self.total = debit - credit

	def getDate(self):
		return self.date

	def getInvoiceNumber(self):
		return self.invoiceNumber

	def getCity(self):
		return self.city

	def getTotal(self):
		return self.total 

	def summarize(self):
		return "{date: " + str(self.date) + ", invoice number: " + self.invoiceNumber + ", city: " + self.city + ", total: " + str(self.total) + "}"