import smtplib
from getpass import getpass
import stdiomask
import sys
server=smtplib.SMTP("smtp.gmail.com",587)    
server.starttls()
server.ehlo()
def main(fromEmail,password,toEmail,message):
    server.login(fromEmail,password)
    try:
        server.sendmail(fromEmail,toEmail,message)
        print("message or feedback sent")
    except:
        print("error sending message or feedback")
    server.quite()
fromEmail=input("fromEmail:")
password=stdiomask.getpass()
toEmail=("yourmail@gmail.com")
message=input("Feedback or message:")
main(fromEmail,password,toEmail,message)
