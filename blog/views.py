from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {'author': 'Ed Radcliffe',
    'title': 'Blog post 1',
    'content': 'Content of first post',
    'date_posted': '31 July 2024'
    },
    {'author': 'Susan Blair',
    'title': 'Blog post 2',
    'content': 'Content of second post',
    'date_posted': '24 July 2024'
    }
]



# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact'})


