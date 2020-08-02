# from flask import Flask
import smtplib, ssl

# Format for email
from email.message import EmailMessage

# For creating env varibles
import os

# settings.py
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# Sets path from which env varibales are imported from
# OR, explicitly providing path to '.env'
from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

def importEmailing(message):
    # system environment variable and they can be accessed via os.getenv()
    GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
    # Variables
    port = 587  # Other port numbers may not work
    host= "smtp.gmail.com"
    sender_email= "gordon.site.mailing@gmail.com"
    receiver_email= "gordon.site.mailing@gmail.com"
    password= GMAIL_PASSWORD

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = "Someone Contacting Me Through Website"
    msg['To'] = receiver_email
    msg['From'] = sender_email

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP(host, port) as server:
            # secure the connection
            server.starttls(context=context)

            # login into email
            server.login(sender_email, GMAIL_PASSWORD)

            # create the email message
            msg = EmailMessage()
            msg.set_content(message)
            msg['Subject'] = "Checkup Website Contact Form -"
            msg['To'] = receiver_email
            msg['From'] = sender_email

            # send the email
            server.send_message(msg)
            
    except Exception as err:
        print(err)