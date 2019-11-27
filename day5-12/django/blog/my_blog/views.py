from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from django.http import HttpResponse

# Function base view
#def home(request):
#    #return HttpResponse('<h1>Blog Home</h1>')
#    context = {
#        'posts': Post.objects.all()
#    }
#    return render(request, 'my_blog/home.html', context)

# Class base view
class PostListView(ListView):
    model = Post
    template_name = 'my_blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] # Display newest post first#

class PostDetailView(DetailView):
    model = Post
    #Default temlate location: <app>/<model>_<type of object>.html

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    #Default temlate location: <app>/<model>_<type of object>.html
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    #Default temlate location: <app>/<model>_<type of object>.html
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    #Default temlate location: <app>/<model>_<type of object>.html
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def about(request):
    context = {
        'posts': Post.objects.all()
    }
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'my_blog/about.html', context)