from django.core.mail import EmailMessage
from django.conf import settings
import os

def send_welcome_email(user_data):
    """Helper function to send a welcome email with a PDF attachment."""
    subject = "Welcome to Our Service!"
    message = f"""
    Hi {user_data.user_email},

    Thank you for providing your details. We have received your email and phone number.
    Stay tuned for more updates.

    Best regards,
    The Team
    """
    sender = "muthondugithinji@gmail.com"
    recipient_list = [user_data.user_email]

    # Correct PDF path using BASE_DIR
    pdf_path = os.path.join(settings.BASE_DIR, 'asset', 'kise.pdf')

    email = EmailMessage(subject, message, sender, recipient_list)
    
    # Attach the PDF if it exists
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as pdf_file:
            email.attach('kise.pdf', pdf_file.read(), 'application/pdf')

    email.send(fail_silently=False)
