import math
price = math.sqrt(4)
print price

price = 300**0.5
print price

#Split String
stock_index = "SP500"
print stock_index[0:]
print stock_index[0:1] #same as [:1]
print stock_index[1:]
print stock_index[2:]
print stock_index[:1]
print stock_index[:2]

#Using format()

stock_index = "SP500"
price = 300
lowest_price = 100
print("The {} is at {} today.".format(stock_index,price))
print("The {} is at {} today.".format(stock_index,lowest_price))








