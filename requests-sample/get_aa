import requests
import os 
from datetime import date

"""
	sample GET request to alphadvantage api
	ref: https://www.alphavantage.co/documentation/#dailyadj

	better documented api: https://polygon.io/docs/get_vX_reference_options_contracts_anchor
"""
def getAlphaAdvantage():
	API_KEY=os.getenv("ALPHAD_API_KEY")
	ticker='TSLA'
	function= "TIME_SERIES_DAILY_ADJUSTED"

	
	parameters = {
		"apikey" : API_KEY,
		"symbol" : ticker,
		"function" : function,
		# "outputsize" :"compact"
	}

	host = 'https://www.alphavantage.co/query'
	
	response = requests.get(schemeNhost, params=parameters)
	print(response.url)

	if response.status_code == requests.codes.ok:
		print(f"Response received with status: {response.status_code}")
		data = response.json()
		print(data)

		#show metadata
		# metadata=data["Meta Data"]
		# print(metadata)

		#narrow down to todays stock price
		# print(data["Time Series (Daily)"][todayHelper()])

# today in YYYY-MM-DD
def todayHelper():
	today = date.today()	
	return today.strftime("%Y-%m-%d")

getAlphaAdvantage()