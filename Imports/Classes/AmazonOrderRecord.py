from .AmazonRecord import *

class AmazonOrderRecord(AmazonRecord):
	def __init__(self, row, date, cashReceived):
		super().__init__(row, date)
		self.cashReceived = cashReceived
		self.invoiceNumber = ''
		self.cutOff = False

	def getCashReceived(self):
		return self.cashReceived

	def getInvoiceNumber(self):
		return self.invoiceNumber

	def isCutOff(self):
		return self.cutOff

	def summarize(self):
		return "{row: " + str(self.row) + ", date: " + str(self.date) + ", cash received: " + str(self.cashReceived) + ", invoice number: " + self.invoiceNumber + ", cut off: " + str(self.cutOff) + "}"