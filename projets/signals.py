from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Message
import uuid

# @receiver(post_save, sender=Profile)
def createMessage(sender, instance, created, **kwargs):
    print('Profile signal triggered')
    if created:
        message = instance
        """ messageSender = {
            'name' : message.name,
            'email' : message.email,
            'subject' : message.subject,
            'body' : message.body
        } """

        subject = 'Nouveau message reçu'
        messageSe = "Bonjour ! \n\nMerci de m'avoir contacter. Je vous réponds dès que possible.\n\nCordialement, \nMr RAJESWARAN Pirathepan"
        
        send_mail(
            subject,
            messageSe,
            settings.EMAIL_HOST_USER,
            [message.email],
            fail_silently=False,
        )

post_save.connect(createMessage, sender=Message)