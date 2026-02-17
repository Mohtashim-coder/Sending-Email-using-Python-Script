import smtplib
import getpass
from email.mime.text import MIMEText

def send_email():
    sender_address = 'alammohtashim3@gmail.com'
    password = input("App password: ")
    subject = 'Learn.Inspire.Grow.'
    msg = '''

        Hello Everyone!

        I've sent you this mail using python script!

        Thank you!
        Md Mohtashim Alam
    '''
    # server initialisation
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_address, password)
    recipients = ['alammohtashim3@gmail.com', 'alalmohtashim3@gmail.com']

    # draft my message body
    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = sender_address
    msg['To'] = ", ".join(recipients)

    server.sendmail(sender_address, recipients, msg.as_string())

send_email()
