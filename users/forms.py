from .models import UserManager
from django.forms import ModelForm
from django import forms


class RegisterForm(ModelForm):
    user_name = forms.CharField(min_length=4, max_length=50, label='Username', help_text='required')
    email = forms.EmailField(max_length=100, label='email', help_text='required', error_messages={
        'required': 'You must enter an email address'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput, help_text='required')
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput, help_text='required')

    class Meta:
        model = UserManager
        fields = ['user_name', 'email', 'password', 'password2']