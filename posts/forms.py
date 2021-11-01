from django import forms
from django.forms import ModelForm
from .models import Post
    




class CreateToDo(forms.ModelForm):
    
    class Meta:
        model = Post 
        fields = ['title', 'description', 'due_date', 'due_time', 'priority', 'done']
