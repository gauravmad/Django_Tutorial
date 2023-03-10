"""gaurav URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from gaurav import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homepage, name="home"),
    path('services/', views.service,name="service"),
    path('portfolio/', views.portfolio,name="portfolio"),
    path('about/',views.about ,name="about"),
    path('team/',views.team ,name="team"),
    path('pricing/',views.price ,name="price"),
    path('contact/',views.contact,name="contact"),
    path('userform/',views.form,name='form'),
    path('userformPOST/', views.form2,name="form2"),
    path('output/', views.output,name="output"),
    path('calculator/', views.calculator,name="calculator"),
    path('evenodd/', views.evenodd,name="evenodd"),
    path('marksheet/', views.marksheet,name="marksheet"),
    path('newsDetails/<newsid>',views.newsDetails,name="newsDetails")
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)