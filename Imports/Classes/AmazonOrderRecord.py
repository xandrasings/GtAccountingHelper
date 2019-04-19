from .AmazonRecord import *

class AmazonOrderRecord(AmazonRecord):
	def __init__(self, row, date, productSales, shippingCredits, salesTaxCollected, sellingFees, total):
		super().__init__(row, date)
		self.invoiceNumber = ''
		self.cashReceived = productSales + shippingCredits + sellingFees
		self.taxedTotal = shippingCredits + total
		self.cutOff = False

	def getInvoiceNumber(self):
		return self.invoiceNumber

	def getCashReceived(self):
		return self.cashReceived

	def getTaxedTotal(self):
		return self.taxedTotal

	def isCutOff(self):
		return self.cutOff

	def summarize(self):
		return "{row: " + str(self.row) + ", date: " + str(self.date) + ", invoice number: " + self.invoiceNumber + ", cash received: " + str(self.cashReceived) + ", taxed total: " + str(self.taxedTotal) + ", cut off: " + str(self.cutOff) + "}"