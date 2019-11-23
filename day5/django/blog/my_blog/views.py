from django.shortcuts import render
#from django.http import HttpResponse

posts = [{'author':'Ted1', 'date_posted':'29/12/1998', 'title':'1st post', 'content':'Hello world!'},
        {'author':'Ted2', 'date_posted':'29/12/1998', 'title':'2nd post', 'content':'Hello world!'},
        {'author':'Ted3', 'date_posted':'29/12/1998', 'title':'3rd post', 'content':'Hello world!'},
        {'author':'Ted4', 'date_posted':'29/12/1998', 'title':'4th post', 'content':'Hello world!'}
        ]

def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    context = {
        'posts': posts
    }
    return render(request, 'my_blog/home.html', context)

def about(request):
    context = {
        'posts': posts
    }
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'my_blog/about.html', context)