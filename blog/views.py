from django.shortcuts import render
from django.http import HttpResponse

from .models import Post 

title = 'Blog - Home'

posts = Post.objects.all()

def home(request):
    context = {
        'title': title,
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
