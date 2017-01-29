#SMS messaging dependencies 
from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

#email dependencies 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def notify(mobile_no, email_id, location):  
	''' 
	function to notify the emergency contact that the person has fallen down
	notification done via SMS and email 
	SMS notification requires TWILIO   
	'''
	#Twilio account details
	account_sid = "AC21a66fc12242db03208ce94925ef0455" 
	auth_token  = "7ce6ddfbf64ab755f0660ff3eb3f1aea"  

	client = TwilioRestClient(account_sid, auth_token)

	#Send SMS 
	try: 
	    message = client.messages.create(
		    body="A fall has been detected at " + location + "!",
	        to=mobile_no,    
	        from_="+441133207644") 

	except TwilioRestException as e: 
		print(e) 
		print("SMS failed") 

	#email login credentials
	me = "neuralfalldetector@gmail.com"
	my_password = "neuralfall2017" # might need 'r' prefix 

	#message details
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Alert"
	msg['From'] = me
	msg['To'] = email_id

	html = '<html><body><p>A fall has been detected at ' + location + '!</p></body></html>'
	part2 = MIMEText(html, 'html')

	msg.attach(part2)

	#server to send email
	s = smtplib.SMTP_SSL('smtp.gmail.com') 
	s.login(me, my_password)
	s.sendmail(me, email_id, msg.as_string())
	s.quit()




