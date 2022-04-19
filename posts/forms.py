from django import forms
from django.shortcuts import redirect
from .models import Post
from django.utils import timezone


class CreateToDo(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'due_date', 'due_time', 'priority']