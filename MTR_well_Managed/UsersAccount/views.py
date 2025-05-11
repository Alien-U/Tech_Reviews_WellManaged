from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from.models import Profile
from.forms import ProfileForm
from Software.models import Software
from Gaming.models import Gaming
from Electronics.models import Electronics
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.decorators import login_required

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
        login(request, myuser,backend='django.contrib.auth.backends.ModelBackend')#login for authenticating user
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

@login_required
def handleLogout(request):
    logout(request)
    messages.success(request,"successfully logged out")
    return redirect('/')

@login_required
def ProfilePage(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            username=request.user.username
            messages.success(request, f"Profile updated successfully for {username}.")
            return redirect('/')
    else:
        form= ProfileForm(instance=request.user.profile)
    UserPostsSoft=Software.objects.filter(author=request.user)
    UserPostsElect=Electronics.objects.filter(author=request.user)
    UserPostsGame=Gaming.objects.filter(author=request.user)
    user_profile =Profile.objects.get(user=request.user) 
    return render(request, 'UsersAccount/UserProfile.html', {'profile': user_profile,'form': form,'UserPostsSoft':UserPostsSoft,'UserPostsElect':UserPostsElect,'UserPostsGame':UserPostsGame})  # Pass the profile object to the template

def deleteElectpost(request,slug):
    if request.method == "POST":
        CurrentUserPost = Electronics.objects.filter(author=request.user,slug=slug).first()
        CurrentUserPost.delete()
        messages.success(request,"Sucessfully Deleted")
    return redirect('ProfilePage')

def deleteGamepost(request,slug):
    if request.method == "POST":
        CurrentUserPost = Gaming.objects.filter(author=request.user,slug=slug).first()
        CurrentUserPost.delete()
        messages.success(request,"Sucessfully Deleted")
    return redirect('ProfilePage')

def deleteSoftpost(request,slug):
    if request.method == "POST":
        CurrentUserPost = Software.objects.filter(author=request.user,slug=slug).first()
        CurrentUserPost.delete()
        messages.success(request,"Sucessfully Deleted")
    return redirect('ProfilePage')