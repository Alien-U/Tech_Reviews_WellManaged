from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from tinymce.models import HTMLField

# Create your models here.
class Software(models.Model):
    Soft_id_sno = models.AutoField(primary_key=True)
    product_header = models.CharField(max_length=100,default="")
    product_name = models.CharField(max_length=30,default="")
    subcategory=models.CharField(max_length=50,default="")
    desc=HTMLField()
    author = models.CharField(max_length=13,default="")
    slug=models.CharField(max_length=100)
    pub_date = models.DateField()
    image=models.ImageField(upload_to="Software/images",default="")

    def __str__(self):
        return self.product_header+' by '+self.author

class SoftwareComment(models.Model):
    Soft_id_sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    software=models.ForeignKey(Software,on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:13] +'...' +' by ' + self.user.username