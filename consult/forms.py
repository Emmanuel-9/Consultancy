from django import forms

class SubscriptionForm(forms.Form):
    email = forms.EmailField(label='Email address')
    
    
class UpdateProfileForm(forms.Form):
    first_name = forms.CharField(label='First name',max_length=300)
    last_name = forms.CharField(label='Last name', max_length=300)
    email = forms.EmailField(label='Email address')
    image = forms.ImageField()

class BookingForm(forms.Form):
    first_name = forms.CharField(label='First name',max_length=300)
    last_name = forms.CharField(label='Last name', max_length=300)

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
class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50,label='First Name')
    last_name = forms.CharField(max_length=50)
    company = forms.CharField(max_length=250)
    title = forms.CharField(max_length=250)
    email = forms.EmailField(help_text='A valid email address, please.')
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50)
    interest =forms.ChoiceField(choices=INTEREST_CHOICES)
    abouts = forms.ChoiceField(choices=ABOUT_CHOICES)
    questions = forms.CharField(max_length=250,widget=forms.Textarea)
