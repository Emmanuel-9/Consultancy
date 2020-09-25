from django import forms
from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    first_name = forms.CharField(label='First name',max_length=300)
    last_name = forms.CharField(label='Last name', max_length=300)
    email = forms.EmailField(label='Email address')
    phone = PhoneNumberField()