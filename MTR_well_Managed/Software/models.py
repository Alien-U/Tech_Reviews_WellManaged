from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from tinymce.models import HTMLField
from django.utils.text import slugify
# Create your models here.
class Software(models.Model):
    Soft_id_sno = models.AutoField(primary_key=True)
    post_type=models.CharField(max_length=25,default="")
    product_header = models.CharField(max_length=100,default="")
    subcategory=models.CharField(max_length=50,default="")
    desc=HTMLField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    slug=models.CharField(max_length=100, unique=True, blank=True)
    pub_date =models.DateTimeField(default=now)
    image=models.ImageField(upload_to="Software/images",default="")

    def __str__(self):
        return f"{self.product_header} by {self.author.username}"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_header)
            # Ensure uniqueness even with similar headers
            base_slug = self.slug
            counter = 1
            while Software.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

class SoftwareComment(models.Model):
    Soft_id_sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    software=models.ForeignKey(Software,on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:13] +'...' +' by ' + self.user.username