import requests
# from . import get_aa

host="https://jsonplaceholder.typicode.com/posts"
id =1
"""
	Sample POST request
	ref: https://jsonplaceholder.typicode.com/
"""
def postRequest():
	headers={
		"Content-type" : "application/json"
	}
	payload = {
		"title" : "Greetings",
		"body" : "Hello Hackers!",
		"userId" : 1,
		"id" : id
	}

	response = requests.post(host, data=payload, params=headers)
	print(response.url)
	print(response.json())
	print(f"Response received with status: {response.status_code}")

	if response.status_code == requests.codes.ok:
		data = response.json()
		print(data)

def get():
	response = requests.get(host + f'/{id}')
	print(response.url)
	print(response.json())

postRequest()
# get()