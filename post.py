#handles POST requests 
import requests

#accept input from sensors 
#TO BE DONE 

def make_request(mode): 
	payload = {'key1': 'value1', 'key2': 'value2'}
	r = requests.post('http://httpbin.org/get', params=payload)
	print(r.url)
	#TO BE CONT.  

	if mode == 'run':
		print('run')
	elif mode == 'learn': 
		#More code... else: 
		print('learn')
	else: 
		print("Error: Incorrect input to function 'make_request'. Choose either 'run' or 'train' as input") 


