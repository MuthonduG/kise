from django.core.mail import send_mail

def send_welcome_email(userdata):
    """Helper function to send a welcome email to users."""
    subject = "Welcome to Our Service!"
    message = f"""
    Hi {userdata.user_email},

    Thank you for providing your details. We have received your email and phone number.
    Stay tuned for more updates.

    Best regards,
    The Team
    """
    sender = "muthondugithinji@gmail.com"
    recipient_list = [userdata.user_email]

    send_mail(subject, message, sender, recipient_list, fail_silently=False)
