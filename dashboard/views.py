# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import ImageUpload,PostForm,AboutMeForm,AddSkill,AddContact,AddEducation
from dashboard.models import Profile,Skills,ProfileContact,Post
from django.contrib.auth import login,logout,authenticate
import datetime
from django.db.models import Q
from django.contrib import messages
# Create your views here.

def home(request,username):
    user=request.user
    profile=Profile.objects.get(user=user)
    if username != user.username:
        return redirect('profile',username=username)
    else:
        return render(request,'dashboard/home.html',{'user':user,'profile':profile})


def profile(request,username):
    current_user=request.user
    viewer=Profile.objects.get(user=current_user)
    user=get_object_or_404(User,username=username)
    profile=get_object_or_404(Profile,user=User.objects.get(username=username))
    return render(request,'dashboard/profile.html',{'user':user,'profile':profile,'viewer':viewer})


@login_required()
def profile_image_upload(request,username):
    image=False
    user = request.user
    profile = get_object_or_404(Profile,user=User.objects.get(username=username))
    if request.method =='POST':
        form = ImageUpload(request.POST,request.FILES)
        if form.is_valid():
            profile.profile_image=request.FILES['file']
            profile.save()
            return redirect('home',username=profile.user.username)
        else:
            return HttpResponse('please choose an image')
    else:
        form=ImageUpload()
    return render(request,'dashboard/image_upload.html',{'form':form,'profile':profile,'user':user,'image':image})





def uploadskills(request):
    if request.method == 'POST':
        user = request.user
        profile=Profile.objects.get(user=user)
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = profile
            post.save()
            return redirect('home',username=user.username)
        else:
            print (form.errors)
    else:
        form = PostForm()
    return render(request, 'dashboard/uploadvideo.html', {'form': form,})

def edit_video(request,pk):
    user=request.user
    profile=Profile.objects.get(user=user)
    post=Post.objects.get(pk=pk)
    if request.method == 'POST':
        form=PostForm(request.POST,instance=post,)
        if form.is_valid():
            form.save(commit=False)
            form.profile=profile
            form.save()
            return redirect('home',username=profile.user.username)
        else:
            HttpResponse('form is incomplete')
    else:
        form=PostForm(instance=post)
    return render(request,'dashboard/uploadvideo.html',{'form':form,'post':post})


def delete_video(request,pk):
    user=request.user
    post= get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('home',username=user.username)


def aboutme(request,pk):
    user = get_object_or_404(User, pk=pk)
    profile=Profile.objects.get(user=user)

    if request.method=='POST':
        form=AboutMeForm(request.POST)
        if form.is_valid():
            aboutme=form.save(commit=False)
            profile.about_me=request.POST['about_me']
            profile.user=request.user
            profile.save()
            return redirect('home',username=user.username)
        else:
            return HttpResponse (form.errors)
    else:
        form=AboutMeForm()
    return render(request,'dashboard/aboutme.html',{'form':form})



def edit_aboutme(request,pk):
    user = get_object_or_404(User, pk=pk)
    profile=get_object_or_404(Profile,user=user)

    if request.method=='POST':
        form = AboutMeForm(request.POST, instance=profile)
        if form.is_valid():
            aboutme=form.save(commit=False)
            profile.about_me=request.POST['about_me']
            profile.user=request.user
            profile.save()
            return redirect('home',username=user.username)
        else:
            return HttpResponse(form.errors)
    else:
        form=AboutMeForm(instance=profile)
    return render(request,'dashboard/aboutme.html',{'form':form,'profile':profile})




def learning(request):
    return render(request,'dashboard/learning.html',{})


def addskills(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    if request.method =='POST':
        form=AddSkill(request.POST)
        if form.is_valid():
            skill=form.save(commit=False)
            skill.profile=profile
            skill.name=request.POST['name']
            skill.save()
            return redirect('home',username=user.username)
        else:
            HttpResponse('form is incomplete')
    else:
        form=AddSkill()
    return render(request,'dashboard/uploadskills.html',{'form':form})


def edit_skill(request,pk):
    user=request.user
    profile=Profile.objects.get(user=user)
    skill=Skills.objects.get(pk=pk)
    if request.method == 'POST':
        form=AddSkill(request.POST,instance=skill)
        if form.is_valid():
            form.save(commit=False)
            form.profile=profile
            form.save()
            return redirect('/')
        else:
            HttpResponse('form is incomplete')
    else:
        form=AddSkill(instance=skill)
    return render(request,'dashboard/uploadskills.html',{'form':form})

def delete_skill(request,pk):
    user=request.user
    skill= get_object_or_404(Skills,pk=pk)
    skill.delete()
    return redirect('home',username=user.username)



def addcontact(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    if request.method =='POST':
        form=AddContact(request.POST)
        if form.is_valid():
            contact=form.save(commit=False)
            contact.profile=profile
            contact.save()
            return redirect('home',username=user.username)
        else:
            HttpResponse('form is incomplete')
    else:
        form=AddContact()
    return render(request,'dashboard/addcontact.html',{'form':form,'profile':profile,})


def edit_contact(request,pk):
    user=request.user
    profile=Profile.objects.get(user=user)
    contact=ProfileContact.objects.get(profile=profile)
    if request.method == 'POST':
        form=AddContact(request.POST,instance=contact)
        if form.is_valid():
            form.save(commit=False)
            form.profile=profile
            form.save()
            return redirect('home',username=user.username)
        else:
            HttpResponse('form is incomplete')
    else:
        form=AddContact(instance=contact)
    return render(request,'dashboard/addcontact.html',{'form':form,'profile':profile,'contact':contact,})



def delete_contact(request,pk):
    contact= get_object_or_404(ProfileContact,pk=pk)
    contact.delete()
    return redirect('/')




def addeducation(request,pk):
    user = get_object_or_404(User, pk=pk)
    profile=Profile.objects.get(user=user)
    date=datetime.date.today()

    if request.method=='POST':
        form=AddEducation(request.POST)
        if form.is_valid():
            addeducation=form.save(commit=False)
            profile.masters_degree_name=request.POST['masters_degree_name']
            profile.masters_college_name=request.POST['masters_college_name']
            profile.masters_education_from=request.POST['masters_education_from']
            profile.masters_education_till=request.POST['masters_education_till']
            profile.bachelors_degree=request.POST['bachelors_degree']
            profile.bachelors_college_name=request.POST['bachelors_college_name']
            profile.bachelors_education_from=request.POST['bachelors_education_from']
            profile.bachelors_education_till=request.POST['bachelors_education_till']
            profile.High_School_degree=request.POST['High_School_degree']
            profile.High_School_name=request.POST['High_School_name']
            profile.High_School_from=request.POST['High_School_from']
            profile.High_School_till=request.POST['High_School_till']
            profile.Junior_degree=request.POST['Junior_degree']
            profile.Junior_School_name=request.POST['Junior_School_name']
            profile.Junior_School_from=request.POST['Junior_School_from']
            profile.Junior_School_till=request.POST['Junior_School_till']
            profile.user=request.user
            profile.save()
            return redirect('resume',username=user.username)
        else:
            return HttpResponse(form.errors)
    else:
        form=AddEducation()
    return render(request,'dashboard/addeducation.html',{'form':form,'profile':profile,'date':date,})


def edit_education(request,pk):
    user = get_object_or_404(User, pk=pk)
    profile=get_object_or_404(Profile,user=user)

    if request.method=='POST':
        form = AddEducation(request.POST, instance=profile)
        if form.is_valid():
            addeducation=form.save(commit=False)
            profile.user=request.user
            profile.save()
            return redirect('resume',username=user.username)
        else:
            return HttpResponse(form.errors)
    else:
        form=AddEducation(instance=profile)
    return render(request,'dashboard/addeducation.html',{'form':form,'profile':profile})


def user_logout(request):
    logout(request)
    return redirect('/')




def search(request):
    user=request.user
    if request.method=='POST':
        srch=request.POST['search']

        if srch:
            match=Profile.objects.filter(Q(user__first_name__icontains=srch)|
                                         Q(user__username__icontains=srch)|
                                         Q(description__icontains=srch)
                                         )
            if match:
                return render(request,'dashboard/search.html',{'match':match})

            else:
                messages.error(request, 'no result found')
                return render(request, 'dashboard/search.html', {})
        else:
            return redirect('home',username=user.username)
    else:
        return render(request,'dashboard/search.html')




def follow(request,username):
    profile=get_object_or_404(Profile,user=User.objects.get(username=username))
    current_user=request.user
    viewer=Profile.objects.get(user=current_user)
    if current_user.is_authenticated():
        if viewer != profile.user:
            profile.followed_by.add(viewer)
            return redirect('profile',username=profile.user.username)
    return redirect('profile',username=profile.user.username)





def unfollow(request,username):
    profile = get_object_or_404(Profile, user=User.objects.get(username=username))
    current_user = request.user
    viewer=Profile.objects.get(user=current_user)
    if current_user.is_authenticated():
        profile.followed_by.remove(viewer)
        return redirect('profile',username=profile.user.username)
    return redirect('profile',username=profile.user.username)



def liked_page(request,username):
    current_user=request.user
    profile=get_object_or_404(Profile,user=current_user)
    liked_by=current_user.profile.followed_by.all()
    likes=current_user.profile.follows.all()
    return render(request,'dashboard/stars.html',{'user':current_user,'liked_by':liked_by,'likes':likes})

def block(request,username):
    profile=get_object_or_404(Profile,user=User.objects.get(username=username))
    current_user=request.user
    viewer=Profile.objects.get(user=current_user)
    if current_user.is_authenticated():
        if viewer != profile:
            viewer.block.add(profile)
            return redirect('profile',username=profile.user.username)
    return redirect('profile',username=profile.user.username)


def unblock(request,username):
    profile = get_object_or_404(Profile, user=User.objects.get(username=username))
    current_user = request.user
    viewer=Profile.objects.get(user=current_user)
    if current_user.is_authenticated():
        viewer.block.remove(profile)
        return redirect('profile',username=profile.user.username)
    return redirect('profile',username=profile.user.username)