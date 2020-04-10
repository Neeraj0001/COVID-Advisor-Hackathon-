from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth.models import User,auth
from . models import *
# Create your views here.
def index(request):
    return render(request,'index.html')
def fun(request):
    return render(request,'form.html')
def meter(request):
    Data=meter_data.objects.all()
    n=len(Data)
    l=[]
    sum=0
    params={'Data':Data,'n_r':l,'nrow':range(n)}
    return render(request,'meter.html',params)
def h_no(request):
    Data=helpline_data.objects.all()
    n=len(Data)
    
    params={'Data':Data,'n_r':n,'nrow':range(n)}
    return render(request,'h_no.html',params)
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            print(user)
            auth.login(request,user)
            return redirect('/home/')
        else:
            messages.info(request,'Username and Password doesnt exist ')
    else:
        return render(request,'login.html')

def signup(request):
    
    if request.method == "POST":
        F_name=request.POST['F_name']
        L_name=request.POST['L_name']
        username=request.POST['username']
        email=request.POST['email']
      
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():     
                messages.info(request,'Already Exist')
                return redirect('/sign_in/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Already Exist')
                return redirect('/sign_in/')
            else:
                user=User.objects.create_user(first_name=F_name,last_name=L_name,email=email,password=password1,username=username)
                user.save()
     
                return redirect('/log_in/')
        else:
            return redirect('/sign_in/')

    else:
        return render(request,'signup.html')

def news(request):
    Data=news_data.objects.all()
    n=len(Data)
    
    params={'Data':Data,'n_r':n,'nrow':range(n)}
    return render(request,'news.html',params) 


def form(request):
    if request.method == "POST":
        
        F_name=request.POST.get('F_name','')
        Phone_no=request.POST.get('phone_no','')
        address=request.POST.get('address','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip=request.POST.get('zip','')
        desc=request.POST.get('desc','')
        contact=donation_data(Full_name=F_name,Phone_no=Phone_no,City=city,Address=address,Zip=zip,Donation=desc,State=state)
        contact.save()
        print(F_name)
    return render(request,'form.html')

def fun(request):
    return render(request,'fun.html')

def messages(request):
    return render(request,'message.html')    
        
        
        

