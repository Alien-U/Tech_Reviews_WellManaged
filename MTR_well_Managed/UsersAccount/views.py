from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def AccountPage(request):
    return render(request,'UsersAccount/LoginSignup.html')
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