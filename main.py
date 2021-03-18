import smtplib
from smtplib import SMTP
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


# Change the smtp to your provider and the port, im using google address
server: SMTP = smtplib.SMTP('smtp.gmail.com', 25)
server.ehlo()

# Encrypt - This is gonna get the password in the .txt file
with open('password.txt', 'r') as i:
    password: str = i.read()
# Noun-Encrypt
# server.login('mailtest@testing.com', 'password_test')

server.login('mailtest@testing.com', password)

message = MIMEMultipart()
message['From'] = 'your_name'
message['To'] = 'testmail@spam.le'  # You can use your email or just a spam email

message['Subject'] = 'random message'

with open('msg.txt', 'r') as i:
    message = i.read()

message.attach(MIMEText(message, 'plain'))

filename = 'image.jpg'
attachment = open(filename, 'rb')

pay = MIMEBase('application', 'octet-stream')
pay.set_payload(attachment.read())

encoders.encode_base64(pay)
pay.add_header('Content_Disposition', f'i_attachment; filename={filename}')
message.attach(pay)

text: object = message.as_string()
server.sendmail('mailtest@testing.com', 'testmail@spam.le', text)
