from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pictures', default="profile_pictures/placeholder_pfp.webp")
    location = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.username