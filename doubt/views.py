from django.shortcuts import render
from .models import DoubtQuestion, ContactUs, LiveClass, Subject
import datetime
from math import ceil

# Create your views here.
def home(request):
    subjects = Subject.objects.all()
    print(subjects)
    n = len(subjects)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'subject': subjects}
    return render(request, 'index.html', params)

def doubt(request):
    if request.method == 'POST':
        name = request.POST['name']
        title = request.POST['title']
        content = request.POST['content']
        date = datetime.datetime.now()
        doubtquestion = DoubtQuestion(name = name, title = title,  content = content, date = date)
        doubtquestion.save()
    myDoubts = DoubtQuestion.objects.all()
    return render(request, 'doubt.html', {'myDoubts': myDoubts})

def doubtpost(request, id):
    post = DoubtQuestion.objects.filter(post_id = id)[0]
    return render(request, 'doubtpost.html', {'post': post})

def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        contactus = ContactUs(name=name, phone=phone, email= email, message = message)
        contactus.save()
    return render(request ,"contactus.html")

def liveclass(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        subject = request.POST['subject']
        std = request.POST['std']
        liveclass = LiveClass(name=name, phone=phone, email= email, subject=subject, std= std)
        liveclass.save()
    return render( request, "liveclass.html")

def board(request):
    return render(request, 'board.html')