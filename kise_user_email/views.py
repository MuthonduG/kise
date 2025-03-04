from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage  
from .models import UserData
from .serializers import UserDataSerializer

class SendEmailView(APIView):
    def post(self, request):
        serializer = UserDataSerializer(data=request.data)
        
        if serializer.is_valid():
            user_data = serializer.save()

            subject = "Welcome to Our Service!"
            message = f"Hi {user_data.user_email}, please find your attached document."
            sender = "muthondugithinji@gmail.com"
            recipient_list = [user_data.user_email]

            email = EmailMessage(subject, message, sender, recipient_list)

            # Attach file if uploaded
            if user_data.attachment:
                email.attach_file(user_data.attachment.path)

            email.send(fail_silently=False)
            return Response({"message": "Email sent successfully with attachment!"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
