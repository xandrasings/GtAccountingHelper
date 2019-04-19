from .AmazonRecord import *

class AmazonOrderRecord(AmazonRecord):
	def __init__(self, row, date, cashReceived):
		super().__init__(row, date)
		self.cashReceived = cashReceived
		self.invoice = ''
		
	def getCashReceived(self):
		return self.cashReceived

	def getInvoice(self):
		return self.invoice

	def summarize(self):
		return "{row: " + str(self.row) + ", date: " + str(self.date) + ", cash received: " + str(self.cashReceived) +", invoice: " + str(self.invoice) + "}"