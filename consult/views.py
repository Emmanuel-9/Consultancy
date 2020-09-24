from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render (request,'base.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'fees.html')

def coaching(request):
    return render(request, 'coaching.html')                

def corporate(request):
    return render(request,'corporate.html')

def individual(request):
    return render(request,'individual.html')

def family(request):
    return render(request,'family.html')    

def register(request):
    return render(request, 'register.html')
