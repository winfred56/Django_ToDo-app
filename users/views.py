from django.shortcuts import render
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully!')
            form.save()
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)