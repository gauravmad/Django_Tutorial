from django.contrib import admin
from service.models import feature
from service.models import Employ
from service.models import services

class FeatureAdmin(admin.ModelAdmin):
    list_display=('feature_icon','feature_title','feature_desc')
    
admin.site.register(feature,FeatureAdmin) 
# Register your models here.

class EmployAdmin(admin.ModelAdmin):
    list_display=('employ_desc','employ_name','employ_post')

admin.site.register(Employ,EmployAdmin)

class servicesAdmin(admin.ModelAdmin):
    list_display = ['service_icon','service_title','service_desc']

admin.site.register(services,servicesAdmin)  