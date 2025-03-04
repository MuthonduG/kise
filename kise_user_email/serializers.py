import re
from rest_framework import serializers
from .models import UserData

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['user_email', 'user_phone', 'attachment']

    def validate_user_email(self, value):
        """Validate email format using regex."""
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(email_regex, value):  
            raise serializers.ValidationError("Invalid email format.")
        

        
        return value
    
    def validate_user_phone(self, value):  # Corrected method name
        """Validate phone number to be exactly 10 digits."""
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")
        
        return value
