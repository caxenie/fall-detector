#handles POST requests 
import requests  

#accept input from sensors 
#TO BE DONE 

print("Enter Use Mode")
print("Training - enter 'a'")
print("Run application - enter 'b'")

use_mode = input(); 

if use_mode == 'a': 
	payload = {'key1': 'value1', 'key2': 'value2'}
	r = requests.get('http://httpbin.org/get', params=payload)
	print(r.url)
	#TO BE CONT.  
elif use_mode == 'b': 
	#More code... 
else: 
	print("Error: choose either a or b") 
