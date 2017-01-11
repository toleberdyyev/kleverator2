from django.contrib.auth.models import User ,Tag
from django import forms
from .models import Task

class UserForm(forms.ModelForm):
    password =  forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

class TaskForm(forms.ModelForm):
    tagger =  forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Task
        fields = ('title','text','tagger','deadline','price','workers')




