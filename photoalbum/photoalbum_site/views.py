from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, PostImage
from .forms import PostForm
from .filters import PostFilter

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def post (request,slug):
    post = Post.objects.get(slug=slug)
    photos = PostImage.objects.filter(post=post)
    context = {'post': post, 'photos':photos}
    return render(request, 'photoalbum_site/post.html', context)

def posts(request):
    posts = Post.objects.filter(active=True)
    myFilter = PostFilter(request.GET, queryset=posts)
    posts = myFilter.qs

    page = request.GET.get('page')
    paginator = Paginator(posts, 3)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts':posts, 'myFilter':myFilter}
    return render(request, 'photoalbum_site/posts.html', context)

def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]
    context = {'posts':posts}
    return render(request, 'photoalbum_site/index.html', context)

def profile (request):
    return render(request, 'photoalbum_site/profile.html')

# crud

@login_required(login_url='home')
def createPost(request):
    form = PostForm()

    if request.method=='POST':
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context={'form':form}
    return render (request, 'photoalbum_site/post_form.html',context)

@login_required(login_url='home')
def updatePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method=='POST':
        form=PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context={'form':form}
    return render (request, 'photoalbum_site/post_form.html',context)

@login_required(login_url='home')
def deletePost(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method=='POST':
        post.delete()
        return redirect('posts')
    context = {'item':post}
    return render(request, 'photoalbum_site/delete.html', context)

def sendEmail(request):

	if request.method == 'POST':

		template = render_to_string('photoalbum_site/email_template.html',
                                    {'name':request.POST['name'],
                                     'email':request.POST['email'],
                                     'message':request.POST['message'],
                                     })

		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['sonitkach@gmail.com']
			)

		email.fail_silently=False
		email.send()
	return render(request, 'photoalbum_site/email_sent.html')