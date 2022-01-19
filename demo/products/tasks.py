from django.core.mail import send_mail
from celery import shared_task
from demo.settings import EMAIL_HOST_USER

@shared_task
def send_email_task(subject,message,receivers):
	send_mail(subject,message,EMAIL_HOST_USER,receivers)
	return 'Sucess'
