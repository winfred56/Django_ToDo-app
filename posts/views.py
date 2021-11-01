from django.core.checks import messages
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from .models import Post
from .forms import CreateToDo
from django.contrib import messages
import datetime

def home(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = CreateToDo(request.POST)
        if form.is_valid():
            messages.success(request,'New Task Added!')
            form.save()
            return redirect('home')
    else:
        form = CreateToDo()
    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'posts/home.html', context)

class TaskDetail(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'

class AddNew(CreateView):
    template_name = 'posts/create.html'
    context_object_name = 'post'
    model = Post
    fields = ['title', 'description', 'due_date', 'due_time', 'priority', 'done']


class TaskDelete(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = '/'
    
