from django import forms
from .models import Project,WorkExperience,Certification,Interest
import datetime



class WorkExperienceForm(forms.ModelForm):

    class Meta:
        model=WorkExperience
        fields=('organisation','designation',
                'worked_from','worked_till',
                'current','describe',)


class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=('title','year',
                'link',
                'position','description',)

class CertificationsForm(forms.ModelForm):

    class Meta:
        model=Certification
        fields=('title','year',
                'link',
                'cert_image',)

class InterestsForm(forms.ModelForm):

    class Meta:
        model=Interest
        fields=('interest',)


'''








'''