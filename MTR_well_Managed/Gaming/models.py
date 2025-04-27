from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from tinymce.models import HTMLField
from django.utils.text import slugify

# Create your models here.
class Gaming(models.Model):
    Gme_id_sno = models.AutoField(primary_key=True)
    post_type=models.CharField(max_length=25,default="")
    product_header = models.CharField(max_length=100,default="")
    # product_name = models.CharField(max_length=30,default="")
    subcategory=models.CharField(max_length=50,default="")
    desc=HTMLField()
    author = models.CharField(max_length=13,default="")
    slug=models.CharField(max_length=100, unique=True, blank=True)
    pub_date = models.DateTimeField(default=now)
    image=models.ImageField(upload_to="Gaming/images",default="")

    def __str__(self):
        return self.product_header+' by '+self.author

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_header)
            # Ensure uniqueness even with similar headers
            base_slug = self.slug
            counter = 1
            while Gaming.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

class GamingComment(models.Model):
    Gme_id_sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    gaming=models.ForeignKey(Gaming,on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:13] +'...' +' by ' + self.user.username