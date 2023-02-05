from django.db import models

class News(models.Model):
    title=models.CharField(max_length=100)
    news_desc =models.TextField()
    news_image = models.FileField(upload_to="news_images/",max_length=250,null=True,default=None)

# Create your models here.
