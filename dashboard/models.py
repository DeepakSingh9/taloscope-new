from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.conf import settings

import datetime




class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth=models.DateField(blank=True,null=True)
    description=models.CharField(blank=False,null=False,max_length=50,default='not sure')
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 #message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #mobile_number = models.CharField(validators=[phone_regex], blank=True, max_length=128)
    profile_image=models.ImageField(upload_to='profilepic/',blank=True,null=True,default='/../static/images/images/astronaut_home.jpg')
    about_me=models.TextField(max_length=150,blank=True)
    #skills=models.ManyToManyField(Skill,blank=True,null=True,related_name='has_skills')
    place=models.CharField(max_length=20,blank=True,null=True)
    #followed_by=models.ManyToManyField('self',related_name='follows',symmetrical=False)
    masters_degree_name = models.CharField(max_length=150, blank=True, default='')
    masters_college_name = models.CharField(max_length=150, blank=True)
    masters_education_from = models.DateField(blank=True,null=True)
    masters_education_till = models.DateField(blank=True,null=True)
    bachelors_degree = models.CharField(max_length=150, blank=True)
    bachelors_college_name = models.CharField(max_length=150, blank=True)
    bachelors_education_from = models.DateField(blank=True,null=True)
    bachelors_education_till = models.DateField(blank=True,null=True)
    High_School_degree = models.CharField(max_length=150, blank=True)
    High_School_name = models.CharField(max_length=150, blank=True)
    High_School_from = models.DateField(blank=True,null=True)
    High_School_till = models.DateField(blank=True,null=True)
    Junior_degree = models.CharField(max_length=150, blank=True)
    Junior_School_name = models.CharField(max_length=150, blank=True)
    Junior_School_from = models.DateField(blank=True,null=True)
    Junior_School_till = models.DateField(blank=True,null=True)
    followed_by=models.ManyToManyField('self',related_name='follows',symmetrical=False)
    block=models.ManyToManyField('self',related_name='blocked_by',symmetrical=False)




    def __str__(self):
        return self.user.username# -*- coding: utf-8 -*-


# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=128,blank=True)
    created = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.IntegerField(blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True,null=True)
    introduction=models.BooleanField(blank=True,default=False)



    def __str__(self):
        return self.profile.user.username

    class Meta:
        ordering=('-introduction',)


class ProfileContact(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    phone=models.CharField(blank=True,max_length=14)
    city=models.CharField(blank=True,max_length=15)

    def __str__(self):
        return self.profile.user.username

class Skills(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    name=models.CharField(max_length=128,blank=True)
    level=models.IntegerField(blank=True,null=True)


    def __str__(self):
        return self.profile.user.username





