import quandl
from pprint import pprint


class Stock:
    def __init__(self, ticker, dates):
        self.data = quandl.Dataset(ticker).data(params=dates)

    # Function that finds maximum value for attribute in collection
    def find_max(self, attr):
        for index, item in enumerate(self.data, start=0):
            value = getattr(item, attr)
            if index == 0:
                high_value = value
            if value > high_value:
                high_value = value

        return high_value

    def find_min(self, attr):
        for index, item in enumerate(self.data, start=0):
           value = getattr(item, attr)
           if index == 0:
                low_value = value
           if value < low_value:
                low_value = value

        return low_value

    def find_diff(self, attr):
       diff = self.find_max(attr) - self.find_min(attr)
       return diff

    def find_avg(self,attr):
        
        for item in self.data:
            



# ======================= DRIVER CODE =============================



quandl.ApiConfig.api_key = "tRqZ1bqsD-mcjEqaLCGR"

config = {"start_date": "2019-06-28", "end_date": "2019-10-28"}

tesla = Stock("EOD/TSLA", config)

openVal = tesla.find_diff("open")

pprint(openVal)
