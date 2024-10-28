from django.shortcuts import render
from app.form import *
from django.http import HttpResponse
from app.models import *
# Create your views here.
def topichtml(request):
    FTD = TopicForms()
    d = {'FTD':FTD}
    if request.method == 'POST':
        TRSH = TopicForms(request.POST)
        if TRSH.is_valid():
            tn = request.POST['tn']
            TO = Topic.objects.get_or_create(Topic_name = tn)
            return HttpResponse('topic is created')
        else:
            return HttpResponse('not created')
        
    return render(request,'topichtml.html',d)
def Webpages(request):
    WDP = Webforms()
    d = {'WDP': WDP}
    if request.method == 'POST':
        EMS = Webforms(request.POST)
        if EMS.is_valid:
            tn = request.POST['table_name']
            na = request.POST['name']
            ul = request.POST['url']
            em = request.POST['email']
            wb = Topic.objects.get(Topic_name = tn)
            TO = Webpage.objects.get_or_create(topic_name = wb,name = na,url = ul,email = em)
            return HttpResponse('created')
        
        else:
            return HttpResponse('not created')
    return render(request,'Webpages.html',d)

