# File Information
AMAZON = 'Amazon'
QUICKBOOKS = 'QuickBooks'

FILE_TYPES = [
	AMAZON,
	QUICKBOOKS
]

ROW = 'Row'
COLUMN = 'Column'

DATE = 'Date'
HEADER = 'Header'
MAX = 'Max'
NON_ORDER_BUFFER = 'Non Order Buffer'
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
			MAX : 25
		}
	},
	QUICKBOOKS : {
		ROW : {},
		COLUMN : {}
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