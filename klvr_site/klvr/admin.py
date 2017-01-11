from django.contrib import admin
from django.contrib.auth.models import Tag
from .models import *

class TaskAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags','workers')


admin.site.register(Tag)
admin.site.register(Task,TaskAdmin)
# Register your models here.
