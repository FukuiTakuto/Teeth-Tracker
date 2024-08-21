from django.contrib.auth.models import Group
from django.contrib import admin

from .models import User,MediaUploadModel,CalendarModel


admin.site.register(User) 
admin.site.unregister(Group) 
admin.site.register(MediaUploadModel)
admin.site.register(CalendarModel)

class MediaUploadModelAdmin(admin.ModelAdmin):
    list_display = ('image', 'tag')

# Register your models here.
