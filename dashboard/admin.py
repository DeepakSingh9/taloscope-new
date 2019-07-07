# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile,Post,ProfileContact,Skills


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','description','profile_image']
    search_fields=['user__first_name','description']


class PostAdmin(admin.ModelAdmin):
    list_display=['video','title','profile']

class ContactAdmin(admin.ModelAdmin):
    list_display=['phone','city']

class SkillAdmin(admin.ModelAdmin):
    list_display=['name','level','profile']



admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(ProfileContact,ContactAdmin)
admin.site.register(Skills,SkillAdmin)
# Register your models here.
