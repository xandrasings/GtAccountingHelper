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
HEADER = 'Header'
INVOICE_NUMBER = 'Invoice Number'
MARKETPLACE = 'marketplace'
MARKETPLACE_FACILITATOR_TAX = 'Marketplace Facilitator Tax'
MAX = 'Max'
MEMO = 'Memo'
NON_ORDER_BUFFER = 'Non Order Buffer'
NUM = 'Num'
ORDER_CITY = 'order city'
ORDER_ID = 'Order ID'
ORDER_POSTAL = 'order postal'
ORDER_STATE = 'order state'
OTHER = 'other'
OTHER_TRANSACTION_FEES = 'other transaction fees'
PRODUCT_SALES = 'Product Sales'
PROMOTIONAL_REBATES = 'promotional rebates'
QUANTITY = 'quantity'
SALES_TAX_COLLECTED = 'Sales Tax Collected'
SELLING_FEES = 'Selling Fees'
SETTLEMENT_ID = 'settlement id'
SHEET_1 = 'Sheet1'
SHIP_TO_CITY = 'Ship To City'
SHIP_TO_STATE = 'Ship To State'
SHIPPING_CREDITS = 'Shipping Credits'
SKU = 'sku'
SPLIT = 'Split'
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
			CASH_RECEIVED : 25,
			CUT_OFF_SPLIT : 26
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
			13 : PRODUCT_SALES,
			14 : SHIPPING_CREDITS,
			15 : GIFT_WRAP_CREDITS,
			16 : PROMOTIONAL_REBATES,
			17 : SALES_TAX_COLLECTED,
			18 : MARKETPLACE_FACILITATOR_TAX,
			19 : SELLING_FEES,
			20 : FBA_FEES,
			21 : OTHER_TRANSACTION_FEES,
			22 : OTHER,
			23 : TOTAL
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
CUT_OFF_COLOR = 'DDDDDD'
DROP_COUNT_LIMIT = 6
FILE_NAME_MODIFIER = '_updated_'
FILE_NAME_SUFFIX = '.xlsx'
FROZEN = 'frozen'
MAIN = '__main__'
ORDER = 'ORDER'
SOLID = 'solid'
