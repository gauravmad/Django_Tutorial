from django.contrib import admin
from submit.models import contactform


class contactformAdmin(admin.ModelAdmin):
    list_display =['form_name','form_email','form_phone','form_message',]
    
admin.site.register(contactform,contactformAdmin)
# Register your models here.
