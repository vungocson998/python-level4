from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse

def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'my_blog/home.html', context)

def about(request):
    context = {
        'posts': Post.objects.all()
    }
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'my_blog/about.html', context)