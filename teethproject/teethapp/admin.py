from django.contrib.auth.models import Group
from django.contrib import admin

from .models import User,MediaUploadModel


admin.site.register(User) 
admin.site.register(MediaUploadModel)
admin.site.unregister(Group) 

# Register your models here.
