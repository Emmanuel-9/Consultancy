from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label='First name',max_length=300)
    last_name = forms.CharField(label='Last name', max_length=300)
    email = forms.EmailField(label='Email address')
    
    
class UpdateProfileForm(forms.Form):
    first_name = forms.CharField(label='First name',max_length=300)
    last_name = forms.CharField(label='Last name', max_length=300)
    email = forms.EmailField(label='Email address')
    image = forms.ImageField()

class BookingForm(forms.Form):
    first_name = forms.CharField(label='First name',max_length=300)
    last_name = forms.CharField(label='Last name', max_length=300)
    
