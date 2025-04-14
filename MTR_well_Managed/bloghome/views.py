from django.shortcuts import render,HttpResponse,redirect
from.models import Contact

from Electronics.models import Electronics
from Gaming.models import Gaming
from Software.models import Software

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
# def home(request):
#     return render(request,'bloghome/index.html')

def home(request):
    Elect_Scroll=Electronics.objects.all()
    Soft_scroll=Software.objects.all()
    gamescroll=Gaming.objects.all()
    params={'Soft_scroll':Soft_scroll,'Elect_Scroll':Elect_Scroll,'gamescroll':gamescroll,}
    return render(request,'bloghome/index.html',params)

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        subject=request.POST.get('subject','')
        message=request.POST.get('message','')
        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
    return render(request,'bloghome/contact.html')
def about(request):
    return render(request,'bloghome/about.html')

def AccountPage(request):
    return render(request,'bloghome/LoginSignup.html')
def handleSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        Fname = request.POST['Fname']
        Lname = request.POST['Lname']
        Email = request.POST['Email'] 
        Password = request.POST['Password'] 
        #check for errorneous input
        #create the user
        myuser = User.objects.create_user(username,Email,Password)
        myuser.first_name = Fname
        myuser.last_name = Lname
        myuser.save()
        login(request, myuser)#login for authenticating user
        messages.success(request,"Your account has been successfully created")
        return redirect('/')
    else:
        return HttpResponse("404-Not Found")

def handleLogin(request):
    if request.method=='POST':
        Loginusername=request.POST['Loginusername']
        LoginPass= request.POST['LoginPass'] 
        user=authenticate(username=Loginusername,password=LoginPass)
        if user is not None:
           login(request,user)
           messages.success(request,"successfully loggdin")
           return redirect('/')
        else:
           messages.error(request,"Invalid Credentials, Please try again")
           return redirect('/')   
    return HttpResponse("404-Not Found")

def handleLogout(request):
    logout(request)
    messages.success(request,"successfully logged out")
    return redirect('/')
    # return HttpResponse("handleLogout")
def search(request):
    query=request.GET['query']
    allElects=Electronics.objects.filter(product_header__icontains=query)
    allSofts=Software.objects.filter(product_header__icontains=query)
    allGames=Gaming.objects.filter(product_header__icontains=query)
    params={'allElects':allElects,'allSofts':allSofts,'allGames':allGames,'query':query}
    return render(request,'bloghome/search.html',params)