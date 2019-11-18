
import quandl
from pprint import pprint

quandl.ApiConfig.api_key = "tRqZ1bqsD-mcjEqaLCGR"

config = {"start_date": "2019-06-28", "end_date": "2019-10-28"}

stocks = quandl.Dataset('EOD/TSLA').data(params=config)

def find_max(collection):
	for index, item in enumerate(collection, start = 0):
		if index == 0:
			high_value = item
		if item > high_value:
			high_value = item

	return high_value

#create a function that creates stocklist for us
#function should allow us to specify what attribute list
def pluck(collection, attr):
	result = []
	for item in collection:
		val = getattr(item, attr)
		result.append(val)

	return result

def att_avg_ratio(collection, attr1, attr2):
	listuno = []
	listduo = []
	for item in collection:
		valuno = getattr(item,attr1)
		listuno.append(valuno)
		valduo = getattr(item,attr2)
		listduo.append(valduo)
	listunoavg = sum(listuno) / len((listuno))
	listduoavg = sum(listduo) / len((listduo))
	return listunoavg / listduoavg

#create a function that gives you average for a list
def averagelist(list):
	return sum(list) / len(list)






# ======================= DRIVER CODE =============================

#total of all stock open prices
ttl_stocks_open = 0
for stock in stocks:
	ttl_stocks_open = ttl_stocks_open + stock.open

#total of all stocks close prices
ttl_stocks_close = 0
for stock in stocks:
	ttl_stocks_close = ttl_stocks_close + stock.close

#average of all stocks open
avg_stocks_open = ttl_stocks_open/len(stocks)
#average of all stocks close
avg_stocks_close = ttl_stocks_close/len(stocks)
#ratio between avg stocks open and avg stocks close
avg_stocks_ratio_opcl = avg_stocks_open / avg_stocks_close

#set attr at stocks object
setattr(stocks,"avg_stocks_ratio", avg_stocks_ratio_opcl)
setattr(stocks,"avg_stocks_close_attr",avg_stocks_close)
setattr(stocks,"avg_stocks_open_attr",avg_stocks_open)


for stock in stocks:
	avg_stock = (stock.open + stock.close) / 2
	setattr(stock,"avg",avg_stock)


# pprint(att_avg_ratio(stocks,"open","close"))


class EOD


#def calc_avg_ratio(collection, frst_attr, scnd_attr , name):
#	frst_totalval = 0
#	scnd_totalval = 0
#	for item in collection:
#		frst_totalval = frst_totalval + item.frst_attr
#		scnd_totalval = scnd_totalval + item.scnd_attr
#		return collection

#	return ratio
#pprint(calc_ratio(stocks,stock.open,stock.close, "opencloseratio"))
#pprint("TOTAL NUMBER OF MARKET DAYS: " + str(len(stocks)))
#pprint("TOTAL STOCKS OPEN: " + str(ttl_stocks_open))
#pprint("TOTAL STOCKS CLOSE: " + str(ttl_stocks_close))
#pprint("AVG STOCK OPEN: " + str(avg_stocks_open))
#pprint("AVG STOCK CLOSE: " + str(avg_stocks_close))
#pprint("AVG STOCK RATIO: " + str(avg_stocks_ratio_opcl))
#pprint(dir(stocks))
