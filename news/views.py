from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .forms import AddPostForm, RegisterUserForm
from .models import *
from django.views.generic import ListView, CreateView





def aboutUs(request):
    posts = Coments.objects.all()
    return render(request, 'news/about.html', {'posts': posts })

def index(request):
    return render(request, 'news/index.html')

def main(request):
    posts = News.objects.all()
    return render(request, 'news/main.html',  {'posts': posts })

def kino(request):
    posts = Kino.objects.all()
    return render(request, 'news/kino.html', {'posts': posts})

def music(request):
    posts = Music.objects.all()
    return render(request, 'news/music.html', {'posts': posts})

def actor(request):
    posts = Actor.objects.all()
    return render(request, 'news/actor.html', {'posts': posts})

def categories(request, cat):
    return HttpResponse(f"<h1>Статьи по категориям</h1>{cat}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)
    return render(request, 'news/post.html',{'post': post})


def show_post_kino(request, post_slug):
    post = get_object_or_404(Kino, slug=post_slug)
    return render(request, 'news/postkino.html',{'post': post})

def show_post_music(request, post_slug):
    post = get_object_or_404(Music, slug=post_slug)
    return render(request, 'news/postmusic.html',{'post': post})

def show_post_actor(request, post_slug):
    post = get_object_or_404(Actor, slug=post_slug)
    return render(request, 'news/postactor.html',{'post': post})



def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                form.save()
                return redirect('about')
            except:
                form.add_error(None, 'Ошибка добавления комментария')
    else:
        form = AddPostForm()
    return render(request, 'news/addpage.html', {'form': form })


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'news/register.html'
    success_url = reverse_lazy('login')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'news/login.html'

def logout_user(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request, 'news/profile.html')







