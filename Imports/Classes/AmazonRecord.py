class AmazonRecord:
	def __init__(self, row, salesTax, total):
		self.row = row
		self.cashReceived = row + salesTax
		self.invoiceNumber = 0

	def getRow(self):
		return self.row

	def getCashReceived(self):
		return self.cashReceived

	def getInvoiceNumber(self):
		return self.invoiceNumber

	def setInvoiceNumber(self, invoiceNumber)
		self.invoiceNumber = invoiceNumber

	def summarize(self):
		return "{row: " + str(self.row) + ", cash_received: " + str(self.cashReceived) + ", invoice_number: " + str(self.invoiceNumber) + "}"