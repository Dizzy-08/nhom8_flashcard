from django.db import models
from django.contrib.auth.models import User # use Django's default user model

class Profile(models.Model):  # Create a Profile model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
