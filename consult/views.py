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
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm() 
    return render(request, 'services/services.html',{"form": form})

def about(request): 
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm()     

    return render(request, 'about/about.html',{"form": form})


def case_studies(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm() 
    return render(request, 'case_studies.html',{"form": form})                

def questions(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm() 
    return render(request, 'questions.html',{"form": form})



def blog(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm() 
    return render(request, 'blog.html',{"form": form})

def approach(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm() 
    return render(request,'about/approach.html',{"form": form})

def career(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm() 
    return render(request,'about/careers.html',{"form": form})

def purpose(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm() 
    return render(request,'about/purpose.html',{"form": form})

def recognition(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm() 
    return render(request,'about/recognition.html',{"form": form})

def team(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm() 
    return render(request,'about/team.html',{"form": form})

def building(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm() 
    return render(request,'services/building.html',{"form": form})

def change(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm() 
    return render(request,'services/change.html',{"form": form})

def conflict(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm() 
    return render(request,'services/conflict.html',{"form": form})

def digital(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm() 
    return render(request,'services/digital.html',{"form": form})

def leadership(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm() 
    return render(request,'services/leadership.html',{"form": form})

def talent(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm() 
    return render(request,'services/talent.html',{"form": form})                    

def contact(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = SubscriptionForm()      
    return render(request,'contact.html',{"form": form})



 