from django.shortcuts import render
from .models import DoubtQuestion, ContactUs, LiveClass

# Create your views here.
def home(request):
    return render(request, 'index.html')

def doubt(request):
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
        std = request.POST.get['std']
        liveclass = LiveClass(name=name, phone=phone, email= email, subject=subject, std= std)
        liveclass.save()
    return render( request, "liveclass.html")