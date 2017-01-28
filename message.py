#SMS messaging dependencies 
from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

#email dependencies 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Twilio account details
account_sid = "AC21a66fc12242db03208ce94925ef0455" 
auth_token  = "7ce6ddfbf64ab755f0660ff3eb3f1aea"  

client = TwilioRestClient(account_sid, auth_token)

#Send SMS 
try: 
    message = client.messages.create(
    	body="A fall has been detected!",
        to="+447599463432",    
        from_="+441133207644") 

except TwilioRestException as e: 
   print(e) 
   print("SMS failed") 

#email login credentials
me = "neuralfalldetector@gmail.com"
my_password = "neuralfall2017" # might need 'r' prefix 
you = "markmathews212@gmail.com"

#message details
msg = MIMEMultipart('alternative')
msg['Subject'] = "Alert"
msg['From'] = me
msg['To'] = you

html = '<html><body><p>A fall has been detected!</p></body></html>'
part2 = MIMEText(html, 'html')

msg.attach(part2)

#server to send email
s = smtplib.SMTP_SSL('smtp.gmail.com') 
s.login(me, my_password)
s.sendmail(me, you, msg.as_string())
s.quit()
