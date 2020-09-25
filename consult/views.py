from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from .forms import ContactForm

# Create your views here.
def home(request):
    return render (request,'base.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = ContactForm()        

    return render(request, 'contact.html')

def fees(request):
    return render(request, 'fees.html')

def coaching(request):
    return render(request, 'coaching.html')                

def questions(request):
    return render(request, 'questions.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('login')
    else:
        form = UserCreationForm()


    return render(request, 'registration/registration_form.html',{"form": form})

@login_required(login_url='accounts/login')
def profile(request):
    return render(request, 'profile.html')