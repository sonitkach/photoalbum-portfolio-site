from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def post (request,pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'photoalbum_site/post.html', context)

def posts(request):
    posts = Post.objects.filter(active=True)
    context = {'posts':posts}
    return render(request, 'photoalbum_site/posts.html', context)

def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]
    context = {'posts':posts}
    return render(request, 'photoalbum_site/index.html', context)

def profile (request):
    return render(request, 'photoalbum_site/profile.html')


