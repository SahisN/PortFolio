import smtplib
from email.message import EmailMessage
import os


# A emailing bot that can perform various email related tasks
class MailBot:
    sender = "jarvismark01v@gmail.com"
    credential = os.environ.get("PASSWORD")

    def __init__(self, receiver, subject, content):
        self.receiver = receiver
        self.subject = subject
        self.content = content

    # Normal text email
    def send_email(self):
        email = EmailMessage()

        # Email From, Email To
        email["from"] = "Jarvis"
        email["To"] = self.receiver
        email["subject"] = self.subject
        email.set_content(self.content)

        # Sending email via gmail
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(MailBot.sender, MailBot.credential)
            smtp.send_message(email)
