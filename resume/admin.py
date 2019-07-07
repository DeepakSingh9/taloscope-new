# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project,WorkExperience,Certification,Interest

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['profile','title','year','description','link','position']

class WorkexpAdmin(admin.ModelAdmin):
    list_display = ['profile','organisation','designation','worked_from','worked_till','current','describe']


class CertificationAdmin(admin.ModelAdmin):
    list_display = ['profile','title','link','cert_image','year']

class InterestAdmin(admin.ModelAdmin):
    list_display = ['profile','interest']

admin.site.register(Project,ProjectAdmin)
admin.site.register(WorkExperience,WorkexpAdmin)
admin.site.register(Certification,CertificationAdmin)
admin.site.register(Interest,InterestAdmin)


