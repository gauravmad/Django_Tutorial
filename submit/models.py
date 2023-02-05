from django.db import models

# Create your models here.
class contactform(models.Model):
    form_name = models.CharField(max_length=100)
    form_email = models.CharField(max_length=100)
    form_phone = models.CharField(max_length=10)
    form_message = models.TextField()
    