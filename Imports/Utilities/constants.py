# File Information
AMAZON = 'Amazon summary'
QUICKBOOKS = 'QuickBooks summary'
REPORT = 'Report output'

FILE_TYPES = [
	AMAZON,
	QUICKBOOKS,
	REPORT
]

SELF = 'Self'
DIRECTORY = 'Directory'
EXCEL = 'Excel'

ACCEPTS = {
	AMAZON : {
		SELF : False,
		DIRECTORY : True,
		EXCEL : True
	},
	QUICKBOOKS : {
		SELF : False,
		DIRECTORY : True,
		EXCEL : True
	},
	REPORT : {
		SELF : True,
		DIRECTORY : True,
		EXCEL : False
	}
}

SHEET = 'Sheet'
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
PRODUCT_SALES = 'Product Sales'
SALES_TAX_COLLECTED = 'Sales Tax Collected'
SELLING_FEES = 'Selling Fees'
SHEET_1 = 'Sheet1'
SHIPPING_CREDITS = 'Shipping Credits'
TOTAL = 'Total'
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
			PRODUCT_SALES : 13,
			SHIPPING_CREDITS : 14,
			SALES_TAX_COLLECTED : 17,
			SELLING_FEES : 19,
			TOTAL : 23,
			MAX : 23,
			INVOICE_NUMBER : 24,
			CASH_RECEIVED : 25
		}
	},
	QUICKBOOKS : {
		SHEET : SHEET_1,
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
UNAVAILABLE_BALANCE = 'Unavailable Balance'

AMAZON_SUMMARY_DATA_TYPES = [
	UNAVAILABLE_BALANCE
]

# Miscellanea
BACK = 'back'
CURRENT_DIRECTORY = 'Current Directory'
FILE_NAME_MODIFIER = '_updated_'
FILE_NAME_SUFFIX = '.xlsx'
FROZEN = 'frozen'
MAIN = '__main__'
ORDER = 'ORDER'