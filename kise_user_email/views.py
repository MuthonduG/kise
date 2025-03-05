from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage  
from .models import UserData
from .serializers import UserDataSerializer
from .signals import send_welcome_email

class SendEmailView(APIView):
    def post(self, request):
        serializer = UserDataSerializer(data=request.data)
        
        if serializer.is_valid():
            user_data = serializer.save()
            send_welcome_email(user_data)  # ✅ Pass the user_data argument
            return Response({"message": "Email sent successfully with attachment!"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
