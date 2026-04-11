from django.contrib.auth.models import AbstractUser 
from django.db import models

class CustomUser(AbstractUser):
    #we use AbstractUser to extend the default user model(password, email, username, etc) and add custom fields if needed
    email = models.EmailField(unique=True)
    username = models.CharField(min_length=3,max_length=20, uique=True)
    bio  = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True, null=True)

    EMAIL_FIELD = "email"
    SURNAME_FIELD = "username"

    def __str__(self):
        return self.username

