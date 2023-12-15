from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    def __str__(self):
        return self.user.username

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="profilepic.jpg", upload_to="profile_picture")
    # image field is not present by-default in django. So,after this line we need to install pillow,
    # in cmd 'pip install pillow'
    location = models.CharField(max_length=100)
