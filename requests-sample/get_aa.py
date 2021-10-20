import requests
import os 
from datetime import date

"""
	sample GET request to alphadvantage api
	ref: https://www.alphavantage.co/documentation/#dailyadj
"""
def getAlphaAdvantage():
	API_KEY=os.getenv("ALPHAD_API_KEY") # replace with oyur API KEY, get one from ref above
	ticker='TSLA'
	function= "TIME_SERIES_DAILY_ADJUSTED"

	
	parameters = {
		"apikey" : "API_KEY",
		"symbol" : ticker,
		"function" : function,
		# "outputsize" :"compact"
	}

	host = 'https://www.alphavantage.co/query'
	
	response = requests.get(host, params=parameters)
	print(response.url)

	if response.status_code == requests.codes.ok:
		print(f"Response received with status: {response.status_code}")
		data = response.json()
		# print(data)

		#show metadata
		metadata=data["Meta Data"]
		print(metadata)

		#narrow down to last refreshed  stock price
		print(data["Time Series (Daily)"][metadata['3. Last Refreshed']])

# today in YYYY-MM-DD
def todayHelper():
	today = date.today()	
	return today.strftime("%Y-%m-%d")

getAlphaAdvantage()