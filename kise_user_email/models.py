from django.db import models

class UserData(models.Model):
    user_email = models.EmailField(unique=True) 
    user_phone = models.CharField(max_length=10, blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to='uploads/', blank=True, null=True)  # New field
