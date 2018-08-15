from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.URLField(blank=True)
    profile_pic = models.ImageField(default='default/Default_avatar.jpg', upload_to='user/avatar/')

    def __str__(self):
        return self.user.username
