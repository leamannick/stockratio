from pprint import pprint

# Version 1 of summing array
pprint("NOT USING FUNCTIONS")
calc1 = [2, 1, 5, 7, 4, 2, 1, 6]
total1 = 0
for num in calc1:
	total1 = total1 + num
pprint("TOTAL 1: " + str(total1))


# Version 2 of summing array
calc2 = [5, 34, 7, 9, 2, 2, 1, 12]
total2 = 0
for num in calc2:
	total2 = total2 + num
pprint("TOTAL 2: " + str(total2))


def sum_list(our_list):
	total = 0
	for n in our_list:
		total = total + n
	return total


# after func. reprint version 1 and 2 of summing
pprint("USING FUNCTIONS")
func_total1 = sum_list(calc1)
pprint("FUNC TOTAL 1: " + str(func_total1))

func_total2 = sum_list(calc2)
pprint("FUNC TOTAL 2: " + str(func_total2))




class Stock:
	open = 5
	close = 6


demo_stock = Stock()

pprint(demo_stock.close)
