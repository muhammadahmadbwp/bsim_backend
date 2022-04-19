from django.conf import settings
from django.core.mail import EmailMessage
import threading

class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=False)

class SendEmail:

    @staticmethod
    def send_email(data):
        subject = data['subject']
        message = data['message']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = data['recipient_list']
        email = EmailMessage(subject=subject, body=message, to=recipient_list)
        email.content_subtype = 'html'
        EmailThread(email).start()