from django.shortcuts import render, redirect, get_object_or_404
from Gaming.models import Gaming 
from Electronics.models import Electronics 
from Software.models import Software
from django.utils.text import slugify  
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib import messages
from tinymce.models import HTMLField
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

@login_required
def Start_Your_Post(request):
    fn=ProductForm()
    if request.method == "POST":
        product_header = request.POST.get('product_header')
        subcategory = request.POST.get('subcategory')
        desc = request.POST.get('desc')
        image = request.FILES.get('image')
        post_type = request.POST.get('post_type')
        # Create a new instance of your model

        if post_type == "Electronics":
            # Create a new instance of the Electronics model
            new_post = Electronics(
                product_header=product_header,
                subcategory=subcategory,
                desc=desc,
                author=request.user,
                image=image,
            )
        elif post_type == "Softwares":
            # Create a new instance of the Electronics model
            new_post = Software(
                product_header=product_header,
                subcategory=subcategory,
                desc=desc,
                author=request.user,
                image=image,
            )
        elif post_type == "Gaming":

            new_post = Gaming(
            product_header=product_header,
            subcategory=subcategory,
            desc=desc,
            author=request.user,
            image=image,
        )
        # Save the new model instance to the database
        new_post.save()

        messages.success(request,"Sucessfully Posted")
    return render(request, 'Write_Your_Blog/Start_Your_Post.html',{'form':fn})