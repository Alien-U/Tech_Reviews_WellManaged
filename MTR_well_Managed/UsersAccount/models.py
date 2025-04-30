from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    Image=models.ImageField(default='UsersAccount/images/default.png',upload_to='UsersAccount/images')

    def __str__(self):
        return f'{self.user.username} Profile'