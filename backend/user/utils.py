
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def emailBookingNotification(request, obj):
    context = {
        'user': obj.first_name,
        'choice':obj.choice
    }
    template = render_to_string('email_template.html', context)

    email = EmailMessage(
        'Notification- A client has booked a session',
        template,
        settings.EMAIL_HOST_USER,
        ['admin@admin.com',],
    )

    email.fail_silently=False
    email.send()