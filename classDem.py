import quandl

quandl.ApiConfig.api_key = "tRqZ1bqsD-mcjEqaLCGR"
config = {"start_date": "2019-06-28", "end_date": "2019-10-28"}

class Stock:

	def __init__(self, ticker, dates):
		self.data = quandl.Dataset(ticker).data(params=dates)

	def pluck(self, attr):
		result = []
		for item in self.data:
			val = getattr(item, attr)
			result.append(val)

		return result





apple = Stock("EOD/AAPL", config)
tesla = Stock("EOD/TSLA", config)
apple.pluck("open")
tesla.pluck("open")

# tickerList = [1,2,3]
# for ticker in tickerList:
# 	stocks = new Ticker(ticker)
# 	pprint(stocks.volatility())

