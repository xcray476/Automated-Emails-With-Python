import smtplib
import ssl 
from email.message import EmailMessage

email_sender = 'codelessearnmore@email.com'
email_password = 'write-password-here'
email_receiver = 'write-email-receiver-here'

subject = 'Check out my new video'
body = """
I've just published a new video on Youtube: https://www.youtube.com/watch?v=HIj8wU_rGIU
"""
em = EmailMessage ()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context ()