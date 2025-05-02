from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    Image=models.ImageField(default='UsersAccount/images/default.png',upload_to='UsersAccount/images')
    my_edited_name = models.CharField(max_length=100, default='')
    Desc=models.TextField(max_length=10000,default='')

    def save(self, *args, **kwargs):
        if not self.my_edited_name and self.user:  # Set default only if it hasn't been provided
            self.my_edited_name = self.user.username  # Or `self.user.get_full_name()` for full name
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} Profile'