 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from dashboard.models import Profile
from .forms import LoginForm, RegisterationForm,ContactForm
from django.contrib import messages
from signup.models import Contact
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.


def user_signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home',username=user.username)
        else:
            messages.error(request,'invalid login details')
            return redirect('signin')
    else:
        form=LoginForm()

    return render(request,'signin.html', {'form':form})




def user_registration(request):
    if request.method == 'POST':
        userlogin = LoginForm(request.POST)
        userregister = RegisterationForm(request.POST)

        if userlogin.is_valid() and userregister.is_valid():
            if User.objects.filter(email=request.POST['email']).exists():
                messages.error(request,'email already exist,try login')

            else:
                user = userlogin.save(commit=False)
                user.set_password(user.password)
                user.save()

                profile = userregister.save(commit=False)
                profile.user = user
                profile.save()

                login(request, authenticate(username=userlogin.cleaned_data['username'],
                                        password=userlogin.cleaned_data['password']))
                return redirect('home',username=request.POST['username'])
        else:
            messages.error(request,userlogin.errors)
    else:
        userlogin = LoginForm()
        userregister = RegisterationForm()
    return render(request,'signup.html', {'userlogin': userlogin, 'userregister': userregister})



def user_logout(request):
    logout(request)
    return redirect('')


def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        sender=request.POST['sender']
        message=request.POST['message']
        form=ContactForm(request.POST)

        if form.is_valid():
            subject='contact form email'
            from_email=settings.DEFAULT_FROM_EMAIL
            to_email=[settings.DEFAULT_FROM_EMAIL]

            contact_message="{0},from{1} with email{2}".format(message,name,sender)

            send_mail(subject,contact_message,from_email,to_email)
            return redirect('contact')

    else:
        form=ContactForm()

    return render(request,'contact.html',{'form':form})




