from django.shortcuts import render
from django.http import HttpResponse

title = 'Blog - Home'

posts = [
    {
        'author': 'Gaurav Gandhi',
        'title': 'First blog',
        'content': 'First post content',
        'date_posted': 'Feb 25, 2021'
    }, {
        'author': 'Gaurav Gandhi',
        'title': 'Second blog',
        'content': 'Second post content',
        'date_posted': 'Feb 26, 2021'
    }
]

def home(request):
    context = {
        'title': title,
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
