from django.db import models

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    fees = models.IntegerField()
    
    


class Facilitator(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    service = models.CharField(max_length=30,null=True)
    contact = models.CharField(max_length=50)

INTEREST_CHOICES = (
    ("Team Building","Team Building"),
    ("Digital Marketing","Digital Marketing"),
    ("Talent Empowerment","Talent Empowerment"),
    ("Leadership","Leadership"),
    ("Change Management","Change Management"),
    ("Conflict Resolution","Conflict Resolution"),
)  
ABOUT_CHOICES = (
    ("None","None"),
    ("Referral","Referral"),
    ("Conference","Conference"),
    ("Networking event","Networking event"),
    ("Search Engine(Yahoo/Google/Bing,etc)","Search Engine(Yahoo/Google/Bing,etc)"),
    ("Email Marketing","Email Marketing"),
    ("Others(please specify below)","Others(please specify below"),
)  
class ContactForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    interest = models.CharField(max_length=250,choices=INTEREST_CHOICES)
    abouts = models.CharField(max_length=250,choices=ABOUT_CHOICES)
    questions_comments = models.TextField()