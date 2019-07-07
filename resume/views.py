# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import WorkExperienceForm,ProjectForm,CertificationsForm,InterestsForm
#,InterestsForm,CertificationsForm
from dashboard.models import Profile
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.models import User
from .models import WorkExperience,Project,Certification,Interest

# Create your views here.

def resume(request,username):
    if request.user.username == username:
        current_user=request.user
        viewer=Profile.objects.get(user=current_user)
        user=request.user
        profile=Profile.objects.get(user=user)
        masters=profile.masters_degree_name
        bachelors=profile.bachelors_degree
        high_school=profile.High_School_degree
        junior_school=profile.Junior_degree
        return render(request,'resume/resume.html',{'user':user,'profile':profile,'masters':masters,'bachelors':bachelors,'high_school':high_school,'junior_school':junior_school,'viewer':viewer})
    else:
        current_user=request.user
        viewer=Profile.objects.get(user=current_user)
        profile = Profile.objects.get(user=User.objects.get(username=username))
        user=get_object_or_404(User,username=username)
        masters = profile.masters_degree_name
        bachelors = profile.bachelors_degree
        high_school = profile.High_School_degree
        junior_school = profile.Junior_degree
        return render(request, 'resume/profileresume.html',
                      {'user':user,'profile': profile, 'masters': masters, 'bachelors': bachelors,
                       'high_school': high_school, 'junior_school': junior_school,'viewer':viewer})




def workexp(request):
    user=request.user
    profile=get_object_or_404(Profile,user=user)
    if request.method== 'POST':
        form=WorkExperienceForm(request.POST)
        if form.is_valid():
            workex=form.save(commit=False)
            workex.profile=profile
            workex.save()
            return redirect('resume',username=profile.user.username)
        else:
            HttpResponse('please fill the form')
    else:
        form=WorkExperienceForm()
    return render(request,'resume/workexp.html',{'form':form,'profile':profile})


def edit_workexp(request,pk):
    user = request.user
    workex = WorkExperience.objects.get(pk=pk)
    profile=Profile.objects.get(user=user)
    if request.method == 'POST':
        form=WorkExperienceForm(request.POST,instance=workex)
        if form.is_valid():
            form=form.save(commit=False)
            form.profile=profile
            form.save()
            return redirect('resume',username=user.username)
        else:
            HttpResponse('please fill the form')
    else:
        form=WorkExperienceForm(instance=workex)

    return render(request,'resume/workexp.html',{'form':form,'profile':profile,'workex':workex,})

def delete_workexp(request,pk):

    workexperience=get_object_or_404(WorkExperience,pk=pk)
    workexperience.delete()
    return redirect('resume',username=workexperience.profile.user.username)



def project(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    if request.method=='POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            project=form.save(commit=False)
            project.profile=profile
            project.save()
            return redirect('resume',username=profile.user.username)
        else:
            HttpResponse('please fill the form')
    else:
        form=ProjectForm()
    return render(request,'resume/projects.html',{'form':form})


def edit_project(request,pk):
    user=request.user
    profile=Profile.objects.get(user=user)
    project=Project.objects.get(pk=pk)
    if request.method == 'POST':
        form=ProjectForm(request.POST,instance=project)
        if form.is_valid():
            project=form.save(commit=False)
            project.profile=profile
            project.save()
            return redirect('resume',username=project.profile.user.username)
        else:
            HttpResponse('please fill the form')
    else:
        form=ProjectForm(instance=project)
    return render(request,'resume/projects.html',{'form':form,'profile':profile,'project':project,})

def delete_project(request,pk):
    project=get_object_or_404(Project,pk=pk)
    project.delete()
    return redirect('resume',username=project.profile.user.username)



def certification(request):
    if request.method == 'POST':
        form=CertificationsForm(request.POST,request.FILES)
        user=request.user
        profile=get_object_or_404(Profile,user=user)
        if form.is_valid():
            certification=form.save(commit=False)
            certification.profile=profile
            certification.save()
            return redirect('resume',username=profile.user.username)
        else:
            HttpResponse('form is incomplete ')
    else:
        form=CertificationsForm()
    return render(request,'resume/certification.html',{'form':form})



def edit_certification(request,pk):
    cert=get_object_or_404(Certification,pk=pk)
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        form=CertificationsForm(request.POST,request.FILES,instance=cert)

        if form.is_valid():
            cert=form.save(commit=False)
            cert.profile=profile
            cert.save()
            return redirect('resume',username=cert.profile.user.username)
        else:
            HttpResponse('form is incomplete ')
    else:
        form=CertificationsForm(instance=cert)
    return render(request,'resume/certification.html',{'form':form,'cert':cert,})

def delete_certification(request,pk):
    certification=get_object_or_404(Certification,pk=pk)
    certification.delete()
    return redirect('resume',username=certification.profile.user.username)




def interest(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    if request.method =='POST':
        form=InterestsForm(request.POST)
        if form.is_valid():
            interest=form.save(commit=False)
            interest.profile=profile
            interest.save()
            return redirect('resume',username=profile.user.username)
        else:
            HttpResponse('form is incomplete')
    else:
        form=InterestsForm()
    return render(request,'resume/interest.html',{'form':form})

def edit_interest(request,pk):
    user=request.user
    profile=Profile.objects.get(user=user)
    interest=Interest.objects.get(pk=pk)
    if request.method == 'POST':
        form=InterestsForm(request.POST,instance=interest)
        if form.is_valid():
            form.save(commit=False)
            form.profile=profile
            form.save()
            return redirect('resume',username=profile.user.username)
        else:
            HttpResponse('form is incomplete')
    else:
        form=InterestsForm(instance=interest)
    return render(request,'resume/interest.html',{'form':form})

def delete_interest(request,pk):
    interest= get_object_or_404(Interest,pk=pk)
    interest.delete()
    return redirect('resume',username=interest.profile.user.username)


