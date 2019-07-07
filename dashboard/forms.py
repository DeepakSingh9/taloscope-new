from django import forms
from django.contrib.auth.models import User
from dashboard.models import Profile,Post,Skills,ProfileContact

class ImageUpload(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('profile_image',)




class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','video','introduction')


class AboutMeForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('about_me',)


class AddSkill(forms.ModelForm):
    class Meta:
        model=Skills
        fields=('name','level',)

class AddContact(forms.ModelForm):
    class Meta:
        model=ProfileContact
        fields=('phone','city',)


class AddEducation(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('masters_degree_name','masters_college_name','masters_education_from',
                'masters_education_till','bachelors_degree','bachelors_college_name',
                'bachelors_education_from','bachelors_education_till','High_School_degree','High_School_name','High_School_from','High_School_till','Junior_degree','Junior_School_name','Junior_School_from','Junior_School_till')