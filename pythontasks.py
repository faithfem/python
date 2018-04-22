
#nested lists
#given variable below, use indexing and key calls to grab:
#i. yesterday's SP500 price of 250
#ii. the number 365 nested inside a list nested inside the "info" key
stock_info = {'sp500':{'today':300,'yesterday': 250}, 'info':['Time',[24,7,365]]}
print stock_info.keys() #result is ['info', 'sp500']
print stock_info['sp500'] #result is {'yesterday': 250, 'today': 300}
print stock_info['info'] #result is [24, 7, 365]
print stock_info['info'][1][2] #result is 365 [CORRECT ANSWER]

#Task5
#Create a function called source_finder() that returns the source. For example, the above string passed into the function would return "QUANDL"

def source_finder(s):
    return s.split('--')[-1]
print source_finder("PRICE:345.324:SOURCE--QUANDL")


#PRICE FINDER
#Create a function called price_finder that returns True if the word 'price' is in a string. 
#Your function should work even if 'Price' is capitalized or next to punctuation ('price!')
# first define def

def price_finder(s):
    return 'price' in s.lower()
    #return "PRICE" in s
print price_finder("What is the price?")
print price_finder("What are the prices")
print price_finder("What is the PRICE?") #the s.lower() takes capitalization into account

#Task #6
#Create a function called count_price() that counts the number of times the word "price" 
#occurs in a string. Account for capitalization and if the word price is next to punctuation.

def count_price(s):
    count = 0
    
    for word in s.lower().split():
        if 'price' in word:
            count = count +1
            
    return count
print count_price("The price is too high a price")
print count_price("The PRICE is too high a PRICE to pay such PRICES!")

#TASK #6 SIMPLER METHOD...
def count_prices(s):
    return s.lower().count('price')
print count_prices("I can't pay such PRICES!")


#Task #7
#Create a function called avg_price that takes in a list of 
#stock price numbers and calculates the average 
#(Sum of the numbers divided by the number of elements in the 
#list). 
#It should return a float.
    
def avg_price(stocks):
    return sum(stocks)/len(stocks)
print avg_price([200,1000,30,3000,100,50,500])
print avg_price([3,4,5])
    
#avg_price([200,1000,30,10,3000,100])
#print avg_price
        
        
    
    