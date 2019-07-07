from django.db import models
from django.contrib.auth.models import User
import datetime
from dashboard.models import Profile

# Create your models here.


class Project(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,)
    title= models.CharField(max_length=128)
    year = models.DateField()
    description = models.TextField()
    link = models.URLField(blank=True)
    position=models.CharField(max_length=128,blank=True)

    def __str__(self):
        return self.title


class WorkExperience(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,)
    organisation=models.CharField(max_length=128,blank=True,)
    designation=models.CharField(max_length=128,blank=True,)
    worked_from=models.DateField()
    worked_till=models.DateField(blank=True,null=True,default=datetime.date.today)
    current=models.BooleanField(default=False)
    describe=models.TextField(blank=True)

    def __str__(self):
        return self.organisation

class Certification(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,)
    title=models.CharField(max_length=128)
    year=models.DateField()
    link=models.URLField(blank=True)
    cert_image=models.FileField(upload_to='cert_images/',blank=True)

    def __str__(self):
        return self.title

class Interest(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,)
    interest=models.CharField(max_length=128,blank=True)


    def __str__(self):
        return self.name


'''

class Certification(models.Model):
    education=models.ForeignKey(Education,on_delete=models.CASCADE,)
    title=models.CharField(max_length=128)
    year=models.DateField()
    description=models.TextField()
    link=models.URLField(blank=True)
    cert_image=models.FileField(upload_to='cert_images/',blank=True)

    def __str__(self):
        return self.title







'''