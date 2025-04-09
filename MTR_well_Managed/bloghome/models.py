from django.db import models
from django.utils.timezone import now
# Create your models here.
class Contact(models.Model):
    msg_id_sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    subject=models.CharField(max_length=50,default="")
    message=models.CharField(max_length=300,default="")
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name

    #we have to add comment Section letter 