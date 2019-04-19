# File Information
AMAZON = 'Amazon'
QUICKBOOKS = 'QuickBooks'

FILE_TYPES = [
	AMAZON,
	QUICKBOOKS
]

ROW = 'Row'
COLUMN = 'Column'

CASH_RECEIVED = 'Cash Received'
CITY = 'City'
CREDIT = 'Credit'
DATE = 'Date'
DEBIT = 'Debit'
HEADER = 'Header'
INVOICE_NUMBER = 'Invoice Number'
MAX = 'Max'
NON_ORDER_BUFFER = 'Non Order Buffer'
ORDER_ID = 'Order ID'
TYPE = 'Type'

LOCATION = {
	AMAZON : {
		ROW : {
			HEADER : 8,
			NON_ORDER_BUFFER : 4
		},
		COLUMN : {
			DATE : 1,
			TYPE : 3,
			ORDER_ID : 4,
			CITY : 10,
			MAX : 23,
			CASH_RECEIVED : 24,
			INVOICE_NUMBER : 25
		}
	},
	QUICKBOOKS : {
		ROW : {
			HEADER : 1,
		},
		COLUMN : {
			CITY : 23,
			CREDIT : 21,
			DATE : 7,
			DEBIT : 19,
			INVOICE_NUMBER : 9
		}
	}
}

# Amazon Summary Data
BEGINNING_BALANCE_SUBTOTAL = 'Beginning Balance Subtotal'
ORDERS_SUBTOTAL = 'Orders Subtotal'
REFUNDS_SUBTOTAL = 'Refunds Subtotal'
SHIPPING_SERVICES_SUBTOTAL = 'Shipping Services Subtotal'
TOTAL_BALANCE = 'Total Balance'
UNAVAILABLE_BALANCE = 'Unavailable Balance'
TRANSFER_AMOUNT = 'Transfer Amount'

AMAZON_SUMMARY_DATA_TYPES = [
	BEGINNING_BALANCE_SUBTOTAL,
	ORDERS_SUBTOTAL,
	REFUNDS_SUBTOTAL,
	SHIPPING_SERVICES_SUBTOTAL,
	TOTAL_BALANCE,
	UNAVAILABLE_BALANCE,
	TRANSFER_AMOUNT
]

# Miscellanea
BACK = 'back'
FROZEN = 'frozen'
MAIN = '__main__'
ORDER = 'ORDER'