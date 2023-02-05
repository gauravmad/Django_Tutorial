from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import Userform

from service.models import feature
from service.models import Employ
from service.models import services
from news.models import News
from submit.models import contactform
from django.core.paginator import Paginator
from django.core.mail import send_mail

def homepage(request):
    # send_mail(
    #     'Testing Mail',
    #     'Here is the sample message',
    #     'gauravdeveloper2023@gmail.com',
    #     ['gauravmadan2004@gmail.com'],
    #     fail_silently=False,
    # )
    featureData =feature.objects.all().order_by('feature_title')
    employData = Employ.objects.all()
    newsData = News.objects.all()
    if request.method =="GET":
        st=request.GET.get('servicename')
        if st!=None:
            featureData=feature.objects.filter(feature_title__icontains=st)


    data = {
        'featureData':featureData,
        'employData':employData,
        'newsData': newsData
    }
    return render(request,"index.html",data)

def newsDetails(request,newsid):
    newsDetails = News.objects.get(id=newsid)
    data={
        'newsDetails':newsDetails
    }
    return render(request,'newsdetails.html',data)


def service(request):
    servicesData = services.objects.all()
    paginator =Paginator(servicesData,3)
    page_number =request.GET.get('page')
    servicesDataFinal =paginator.get_page(page_number)
    data ={
        'servicesData':servicesDataFinal
    }
    return render(request,'services.html',data)

def portfolio(request):
    return render(request,'portfolio-details.html')

def about(request):
    return render(request,'about.html')

def team(request):
    return render(request,'team.html')

def price(request):
    return render(request,'pricing.html')

def contact(request):
    feedback=''
    if request.method=="POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        message =request.POST.get('message')
        enquiry =contactform(form_name= name, form_email=email, form_phone=phone, form_message=message)

        enquiry.save()
        feedback="Your Application is successfully sent! &nbsp; We will get back to you soon. &#128512;"
    return render(request,'contact.html',{'feedback':feedback})



def calculator(request):
    c=''
    try:
        if request.method =="POST":
            val1 = eval(request.POST.get('a'))
            val2 = eval(request.POST.get('b'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=val1+val2
            elif opr=="-":
                c=val1-val2
            elif opr=="*":
                c=val1*val2
            elif opr=="/":
                c=val1/val2          
    except:
        c="Invalid Opr..."
    return render(request,'calculator.html',{'c':c})

def evenodd(request):
    d=''
    if request.method=="POST":
        if request.POST.get('a') =="":
            return render(request,'evenodd.html',{'error':True})

        inpt = eval(request.POST.get('a'))
        if inpt%2 == 0:
            d ='Even Number'
        else:
            d ='Odd Number'    

    return render(request,'evenodd.html',{'d':d})            
        
def marksheet(request):
    if request.method == "POST":
        if request.POST.get('subj1') =="":
            return render(request,'marksheet.html',{'error':True})
        sub1 = eval(request.POST.get('subj1'))        
        sub2 = eval(request.POST.get('subj2'))        
        sub3 = eval(request.POST.get('subj3'))

        t = sub1+sub2+sub3
        p = (sub1+sub2+sub3)/3
        if p>=35:
            g="<p style='color:green;'>Congratulations You Pass the examination!!&#128515;</p>"
        else:
            g="<p style='color:red;'>You Failed! Better luck next time &#128549;</p>"
   
        data={
            'total':t,
            'per':p,
            'status':g
        }
        return render(request,'marksheet.html',data)  
    return render(request,'marksheet.html')        


def form(request):
    finalans = 0
    try:
        n1 = int(request.GET['num1'])
        n2 = int(request.GET['num2'])
        finalans= n1+n2
    except:
        pass    
    return render(request,'userform.html',{'output':finalans})

def form2(request):
    finalans1 = 0
    data={}
    try:
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans1= n1*n2
            data = {
                'n1':n1,
                'n2':n2,
                'finaloutput': finalans1
            }
            url="/output/?finaloutput={}".format(finalans1)
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,'userformPOST.html',data)  

def output(request):
    if request.method == "GET":
        output=request.GET.get('finaloutput')
    return render(request,'output.html',{'finaloutput':output})            

