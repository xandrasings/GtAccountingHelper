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

ACCOUNT = 'Account'
CASH_RECEIVED = 'Cash Received'
CITY = 'City'
CLR = 'Clr'
CREDIT = 'Credit'
CUT_OFF_SPLIT = 'Cut Off Split'
DATE = 'Date'
DATE_TIME = 'date/time'
DESCRIPTION = 'description'
DEBIT = 'Debit'
FBA_FEES = 'fba fees'
FULFILLMENT = 'fulfillment'
GIFT_WRAP_CREDITS = 'gift wrap credits'
GIFT_WRAP_CREDITS_TAX = 'giftwrap credits tax'
HEADER = 'Header'
INVOICE_NUMBER = 'Invoice Number'
MARKETPLACE = 'marketplace'
MARKETPLACE_WITHHELD_TAX = 'marketplace withheld tax'
MAX = 'Max'
MEMO = 'Memo'
MIN = 'Min'
NEW_MAX = 'New Max'
NON_ORDER_BUFFER = 'Non Order Buffer'
NUM = 'Num'
ORDER_CITY = 'order city'
ORDER_ID = 'Order ID'
ORDER_POSTAL = 'order postal'
ORDER_STATE = 'order state'
OTHER = 'other'
OTHER_TRANSACTION_FEES = 'other transaction fees'
PRODUCT_SALES = 'Product Sales'
PRODUCT_SALES_TAX = 'product sales tax'
PROMOTIONAL_REBATES = 'promotional rebates'
PROMOTIONAL_REBATES_TAX = 'promotional rebates tax'
QUANTITY = 'quantity'
SELLING_FEES = 'Selling Fees'
SETTLEMENT_ID = 'settlement id'
SHEET_1 = 'Sheet1'
SHIP_TO_CITY = 'Ship To City'
SHIP_TO_STATE = 'Ship To State'
SHIPPING_CREDITS = 'Shipping Credits'
SHIPPING_CREDITS_TAX = 'shipping credits tax'
SKU = 'sku'
SPLIT = 'Split'
TAX_COLLECTION_MODEL = 'tax collection model'
TOTAL = 'Total'
TYPE = 'Type'

LOCATION = {
	AMAZON : {
		ROW : {
			HEADER : 8,
			NON_ORDER_BUFFER : 4
		},
		COLUMN : {
			MIN : 1,
			DATE : 1,
			TYPE : 3,
			ORDER_ID : 4,
			CITY : 10,
			PRODUCT_SALES : 14,
			PRODUCT_SALES_TAX : 15,
			SHIPPING_CREDITS : 16,
			SHIPPING_CREDITS_TAX : 17,
			GIFT_WRAP_CREDITS_TAX : 19,
			PROMOTIONAL_REBATES_TAX : 21,
			MARKETPLACE_WITHHELD_TAX : 22,
			SELLING_FEES : 23,
			TOTAL : 27,
			MAX : 27,
			INVOICE_NUMBER : 28,
			CASH_RECEIVED : 29,
			NEW_MAX : 29,
			CUT_OFF_SPLIT : 30
		},
		HEADER : {
			1 : DATE_TIME,
			2 : SETTLEMENT_ID,
			3 : TYPE,
			4 : ORDER_ID,
			5 : SKU,
			6 : DESCRIPTION,
			7 : QUANTITY,
			8 : MARKETPLACE,
			9 : FULFILLMENT,
			10 : ORDER_CITY,
			11 : ORDER_STATE,
			12 : ORDER_POSTAL,
			13 : TAX_COLLECTION_MODEL,
			14 : PRODUCT_SALES,
			15 : PRODUCT_SALES_TAX,
			16 : SHIPPING_CREDITS,
			17 : SHIPPING_CREDITS_TAX,
			18 : GIFT_WRAP_CREDITS,
			19 : GIFT_WRAP_CREDITS_TAX,
			20 : PROMOTIONAL_REBATES,
			21 : PROMOTIONAL_REBATES_TAX,
			22 : MARKETPLACE_WITHHELD_TAX,
			23 : SELLING_FEES,
			24 : FBA_FEES,
			25 : OTHER_TRANSACTION_FEES,
			26 : OTHER,
			27 : TOTAL
		}
	},
	QUICKBOOKS : {
		SHEET : SHEET_1,
		ROW : {
			HEADER : 1,
		},
		COLUMN : {
			DATE : 7,
			INVOICE_NUMBER : 9,
			DEBIT : 19,
			CREDIT : 21,
			CITY : 23,
			MAX : 25
		},
		HEADER : {
			5 : TYPE,
			7 : DATE,
			9 : NUM,
			11 : MEMO,
			13 : ACCOUNT,
			15 : CLR,
			17 : SPLIT,
			19 : DEBIT,
			21 : CREDIT,
			23 : SHIP_TO_CITY,
			25 : SHIP_TO_STATE
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
CUT_OFF_COLOR = '7e96bc'
DROP_COUNT_LIMIT = 8
FILE_NAME_MODIFIER = '_updated_'
FILE_NAME_SUFFIX = '.xlsx'
FROZEN = 'frozen'
MAIN = '__main__'
ORDER = 'ORDER'
SOLID = 'solid'
