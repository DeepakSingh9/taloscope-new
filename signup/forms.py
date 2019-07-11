from django import forms
from django.contrib.auth.models import User
from dashboard.models import Profile
from signup.models import  Contact



class LoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username','password','first_name','last_name','email',)



class RegisterationForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=('description',)


class ContactForm(forms.ModelForm):

    class Meta:
        model=Contact
        fields=('sender','name','message')

