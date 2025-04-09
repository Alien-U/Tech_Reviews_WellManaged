from django.shortcuts import render,HttpResponse,redirect
from.models import Gaming,GamingComment
from Electronics.templatetags import extras
# Create your views here.
def gaming(request):
    allGaming=Gaming.objects.all()
    # ----------*--------------
    params={'allGaming':allGaming}
    return render(request,'Gaming/Gaming.html',params)


def Gamingpost(request,slug):
    # softscroll=Softwarez.objects.all()
    Gme_scroll=Gaming.objects.all()
    # gamescroll=Gaming.objects.all()
    gaming=Gaming.objects.filter(slug=slug).first()
    comments=GamingComment.objects.filter(gaming=gaming,parent=None)
    replies=GamingComment.objects.filter(gaming=gaming).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.Gme_id_sno not in replyDict.keys():
            replyDict[reply.parent.Gme_id_sno]=[reply]
        else:
            replyDict[reply.parent.Gme_id_sno].append(reply)

    params={'gaming':gaming,'Gme_scroll':Gme_scroll,'comments':comments,'replyDict':replyDict}
    return render(request,'Gaming/Gamingview.html',params)

def postComment(request):
    if request.method=="POST":
        comment=request.POST.get('comment')
        user=request.user
        gamingGme_id_sno=request.POST.get('gamingGme_id_sno')
        gaming=Gaming.objects.get(Gme_id_sno=gamingGme_id_sno)
        Parentsno=request.POST.get("Parentsno")
        if Parentsno=="":
            comment=GamingComment(comment=comment,user=user,gaming=gaming)
        else:
            parent=GamingComment.objects.get(Gme_id_sno=Parentsno)
            comment=GamingComment(comment=comment,user=user,gaming=gaming,parent=parent)
        comment.save()
    return redirect(f'/Gaming/{gaming.slug}')


