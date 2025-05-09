from django.shortcuts import render,HttpResponse,redirect
from.models import Contact
from Electronics.models import Electronics
from Gaming.models import Gaming
from Software.models import Software
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    Elect_Scroll=Electronics.objects.all()
    Soft_scroll=Software.objects.all()
    gamescroll=Gaming.objects.all()
    params={'Soft_scroll':Soft_scroll,'Elect_Scroll':Elect_Scroll,'gamescroll':gamescroll}
    return render(request,'bloghome/index.html',params)

@login_required
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




def search(request):
    query=request.GET['query']
    allElects=Electronics.objects.filter(product_header__icontains=query)
    allSofts=Software.objects.filter(product_header__icontains=query)
    allGames=Gaming.objects.filter(product_header__icontains=query)
    params={'allElects':allElects,'allSofts':allSofts,'allGames':allGames,'query':query}
    return render(request,'bloghome/search.html',params)
