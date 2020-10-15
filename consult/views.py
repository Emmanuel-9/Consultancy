from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SubscriptionForm,ContactForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm() 
    return render (request,'base.html',{"form": form})

def services(request):
    return render(request, 'services/services.html')

def about(request): 
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm()     

    return render(request, 'about/about.html',{"form": form})


def case_studies(request):
    return render(request, 'case_studies.html')                

def questions(request):
    return render(request, 'questions.html')



def blog(request):
    return render(request, 'blog.html')

def approach(request):
    return render(request,'about/approach.html')

def career(request):
    return render(request,'about/careers.html')

def purpose(request):
    return render(request,'about/purpose.html')

def recognition(request):
    return render(request,'about/recognition.html')

def team(request):
    return render(request,'about/team.html')

def building(request):
    return render(request,'services/building.html')

def change(request):
    return render(request,'services/change.html')

def conflict(request):
    return render(request,'services/conflict.html')

def digital(request):
    return render(request,'services/digital.html')

def leadership(request):
    return render(request,'services/leadership.html')

def talent(request):
    return render(request,'services/talent.html')                    

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = ContactForm()  
    return render(request,'contact.html',{"form": form})



 