from django.shortcuts import render,HttpResponse,redirect
from.models import Electronics,ElectronicComment
from Gaming.models import Gaming
from Software.models import Software
from.templatetags import extras
# Create your views here.
def electronics(request):
    allElectronic=Electronics.objects.all()
    # ----------*--------------
    params={'allElectronic':allElectronic}
    return render(request,'Electronics/Electronics.html',params)

def CtegorySort(request):
    category=request.GET['category']
    allElects=Electronics.objects.filter(subcategory__icontains=category)
    params={'allElects':allElects,'category':category}
    return render(request,'Electronics/ElectSort.html',params)

def Electronicpost(request,slug):
    Elect_Scroll=Electronics.objects.all()
    Soft_scroll=Software.objects.all()
    gamescroll=Gaming.objects.all()
    electronics=Electronics.objects.filter(slug=slug).first()
    comments=ElectronicComment.objects.filter(electronics=electronics,parent=None)
    replies=ElectronicComment.objects.filter(electronics=electronics).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.Ele_id_sno not in replyDict.keys():
            replyDict[reply.parent.Ele_id_sno]=[reply]
        else:
            replyDict[reply.parent.Ele_id_sno].append(reply)
    params={'electronics':electronics,'Soft_scroll':Soft_scroll,'Elect_Scroll':Elect_Scroll,'gamescroll':gamescroll,'comments':comments,'replyDict':replyDict}
    return render(request,'Electronics/Electronicsview.html',params)

def postComment(request):
    if request.method=="POST":
        comment=request.POST.get('comment')
        user=request.user
        electronicsEle_id_sno=request.POST.get('electronicsEle_id_sno')
        electronics=Electronics.objects.get(Ele_id_sno=electronicsEle_id_sno)
        Parentsno=request.POST.get("Parentsno")
        if Parentsno=="":
            comment=ElectronicComment(comment=comment,user=user,electronics=electronics)
        else:
            parent=ElectronicComment.objects.get(Ele_id_sno=Parentsno)
            comment=ElectronicComment(comment=comment,user=user,electronics=electronics,parent=parent)
        comment.save()
    return redirect(f'/Electronics/{electronics.slug}')

