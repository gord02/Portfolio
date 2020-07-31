# from flask import Flask
import smtplib, ssl

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
    port = 465  # For SSL
    host= "smtp.gmail.com"
    sender_email= "gordon.site.mailing@gmail.com"
    receiver_email= "gordon.site.mailing@gmail.com"
    password= GMAIL_PASSWORD
  
    print(GMAIL_PASSWORD)
    # Try to log in to server and send email
    try:
        print(GMAIL_PASSWORD)
        # Create a secure SSL context
        context = ssl.create_default_context()
        server = smtplib.SMTP(host, port)
        
        server.starttls(context=context) # Secure the connection
        server.login(sender_email, password)

        # Sends email 
        server.sendmail(sender_email, receiver_email, message)
    except Exception as err:
        # Print any error messages to stdout
        print(err)
    finally:
        server.quit() 