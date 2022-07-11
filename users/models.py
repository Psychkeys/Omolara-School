from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length= 255, null = True, blank = True)
    twitter_url = models.CharField(max_length= 255, null = True, blank = True)

    
    def __str__(self):
        return f'{self.user.username} Profile'


    def __str__(self):
        super().save()

