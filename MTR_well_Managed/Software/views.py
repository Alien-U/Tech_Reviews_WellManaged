from django.shortcuts import render,HttpResponse,redirect
from.models import Software,SoftwareComment
from Gaming.models import Gaming
from Electronics.models import Electronics
from Electronics.templatetags import extras
# Create your views here.
def software(request):
    allSoftware=Software.objects.all()
    # ----------*--------------
    params={'allSoftware':allSoftware}
    return render(request,'Software/Software.html',params)


def Softwarepost(request,slug):
    Elect_Scroll=Electronics.objects.all()
    Soft_scroll=Software.objects.all()
    gamescroll=Gaming.objects.all()
    software=Software.objects.filter(slug=slug).first()
    comments=SoftwareComment.objects.filter(software=software,parent=None)
    replies=SoftwareComment.objects.filter(software=software).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.Soft_id_sno not in replyDict.keys():
            replyDict[reply.parent.Soft_id_sno]=[reply]
        else:
            replyDict[reply.parent.Soft_id_sno].append(reply)

    params={'software':software,'Soft_scroll':Soft_scroll,'Elect_Scroll':Elect_Scroll,'gamescroll':gamescroll,'comments':comments,'replyDict':replyDict}
    return render(request,'Software/Softwareview.html',params)

def postComment(request):
    if request.method=="POST":
        comment=request.POST.get('comment')
        user=request.user
        softwareSoft_id_sno=request.POST.get('softwareSoft_id_sno')
        software=Software.objects.get(Soft_id_sno=softwareSoft_id_sno)
        Parentsno=request.POST.get("Parentsno")
        if Parentsno=="":
            comment=SoftwareComment(comment=comment,user=user,software=software)
        else:
            parent=SoftwareComment.objects.get(Soft_id_sno=Parentsno)
            comment=SoftwareComment(comment=comment,user=user,software=software,parent=parent)
        comment.save()
    return redirect(f'/Software/{software.slug}')


