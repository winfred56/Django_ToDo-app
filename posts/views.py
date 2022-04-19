from django.core.checks import messages
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, DeleteView
from .models import Post
from .forms import CreateToDo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required()
def home(request):
    if request.method == 'POST':
        form = CreateToDo(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            messages.success(request, 'New Task Added!')
            form.save()
            return redirect('/')
    else:
        form = CreateToDo()
    posts = Post.objects.filter(user=request.user)
    context = {
        'posts': posts,
        'form': form
    }

    return render(request, 'posts/home.html', context)


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'


@login_required
def create(request):
    if request.method == 'POST':
        form = CreateToDo(request.POST)
        if form.is_valid():
            #Assigns the author of the post to the current logged in user
            form.instance.user = request.user
            messages.success(request, 'New Task Added!')
            form.save()
            #returns to the post's detail
            return redirect('/')
    else:
        form = CreateToDo()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = '/'