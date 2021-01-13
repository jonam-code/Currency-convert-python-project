# Python lab program - 4/August/2020
# Python program to convert the currency of one currency value to that of another currency value
# Import the modules needed, Requests is a Python module that you can use to send all kinds of HTTP requests. It is an easy-to-use library with a lot of features ranging from passing parameters in URLs to sending custom headers and SSL Verification.
import requests 

print("Python program to convert the currency of one currency value to that of another currency value")
print()
print("Note: please use Upper-case")
print("Example:- AUD, EUR, INR, USD, SUA")
print()

class Currency_convertor: 
	# Empty dictionary to store the exchange rates from json list
	rates = {} 
	def __init__(self, url): 
		data = requests.get(url).json() 

		# Extracting the rates from the json list 
		self.rates = data["rates"] 

	# Function to do the amount conversion  
	def convert(self, from_currency, to_currency, amount): 
		initial_amount = amount 
		if from_currency != 'EUR' : 
			amount = amount / self.rates[from_currency] 

		# Amount calculation and rounding it to 2 decimal places 
		amount = round(amount * self.rates[to_currency], 2) 
    
    #Output using format feature
		print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))

# Driver code 
if __name__ == "__main__": 

	# Public api to get updated exchange rate values
	# Update your access_key by replacing 'ACCESS_KEY'
	# Use can get your free access key by registering in fixer.io
	url = str.__add__('http://data.fixer.io/api/latest?access_key=', 'ACCESS_KEY' ) 
	c = Currency_convertor(url) 
	from_country = input("From: ") 
	to_country = input("To : ") 
	amount = int(input("Amount: ")) 

  # Calling convert fn from Currency_convertor class
	c.convert(from_country, to_country, amount) 



    # Update your access_key by replacing 'ACCESS_KEY'\
    # Use can get your free access key by registering in fixer.io  \
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', 'ACCESS_KEY' ) \
    c = Currency_convertor(url) \
    from_country = input("From: ") \
    to_country = input("To : ") \
    amount = int(input("Amount: ")) \
\
  # Calling convert fn from Currency_convertor class\
    c.convert(from_country, to_country, amount) }
