from .AmazonRecord import *

class AmazonOrderRecord(AmazonRecord):
	def __init__(self, row, date, orderId, city, productSales, shippingCredits, salesTaxCollected, sellingFees, total):
		super().__init__(row, date)
		self.orderId = orderId
		self.city = city
		self.invoiceNumber = ''
		self.cashReceived = productSales + shippingCredits + sellingFees
		self.matchSubtotal = productSales + shippingCredits + salesTaxCollected
		# self.matchSubtotal = productSales + salesTaxCollected
		# self.matchSubtotal = productSales
		self.taxedTotal = salesTaxCollected + total
		self.cutOff = False

	def __eq__(self, other):
		return False

	def __lt__(self, other):
		return self.row < other.row

	def getOrderId(self):
		return self.orderId

	def getCity(self):
		return self.city

	def getInvoiceNumber(self):
		return self.invoiceNumber

	def getCashReceived(self):
		return self.cashReceived

	def getMatchSubtotal(self):
		return self.matchSubtotal

	def getTaxedTotal(self):
		return self.taxedTotal

	def isCutOff(self):
		return self.cutOff

	def setInvoiceNumber(self, invoiceNumber):
		self.invoiceNumber = invoiceNumber

	def setCutOff(self):
		self.cutOff = True

	def summarize(self):
		return "{order id: " + str(self.orderId) + ", city: " + str(self.city) + ", row: " + str(self.row) + ", date: " + str(self.date) + ", invoice number: " + self.invoiceNumber + ", cash received: " + str(self.cashReceived) + ", match subtotal: " + str(self.matchSubtotal) + ", taxed total: " + str(self.taxedTotal) + ", cut off: " + str(self.cutOff) + "}"
