from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from tinymce.models import HTMLField

# Create your models here.
class Gaming(models.Model):
    Gme_id_sno = models.AutoField(primary_key=True)
    product_header = models.CharField(max_length=100,default="")
    product_name = models.CharField(max_length=30,default="")
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=HTMLField()
    author = models.CharField(max_length=13,default="")
    slug=models.CharField(max_length=100)
    pub_date = models.DateField()
    image=models.ImageField(upload_to="Gaming/images",default="")

    def __str__(self):
        return self.product_header+' by '+self.author

class GamingComment(models.Model):
    Gme_id_sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    gaming=models.ForeignKey(Gaming,on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:13] +'...' +' by ' + self.user.username