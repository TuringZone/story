from django.db import models
from accounts.models import UserProfile
from datetime import datetime

# Create your models here.

class Story(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='stories')
    created_on = models.DateTimeField(default=datetime.now)
    content = models.TextField()
    genre = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title + '-' + self.author.user.username
