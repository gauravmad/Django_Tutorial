from django.db import models

class feature(models.Model):
    feature_icon = models.CharField(max_length=50)
    feature_title = models.CharField(max_length=50)
    feature_desc = models.TextField()

# Create your models here.

class Employ(models.Model):
    employ_desc = models.TextField()
    employ_name = models.CharField(max_length=20)
    employ_post = models.CharField(max_length=50)


class services(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_desc =models.CharField(max_length=100)