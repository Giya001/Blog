from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import BLogForms
from blog.models import Blog
from django.db.models import Q


@login_required
def home(request):
    blogs = Blog.objects.filter(published=True)
    search_blog = request.GET.get('search_published_blog')
    if search_blog:
        blogs = Blog.objects.filter(Q(title__icontains=search_blog) | Q(content__icontains=search_blog),
                                    published=True)
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/home.html', context=context)


@login_required
def home_out(request):
    blogs = Blog.objects.filter(published=False)
    search_blog = request.GET.get('search_unpublished_blog')
    if search_blog:
        blogs = Blog.objects.filter(Q(title__icontains=search_blog) | Q(content__icontains=search_blog),
                                    published=False)
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/home_out.html', context=context)


def detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/detail.html', context=context)


def update(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, author=request.user)
    if request.method == 'POST':
        form = BLogForms(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
            if blog.published:
                return redirect('home')
            return redirect('home_out')
    else:
        form = BLogForms(instance=blog)

    return render(request, 'blog/update.html', {'form': form, 'blog': blog})


def create(request):
    if request.method == 'POST':
        form = BLogForms(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            if blog.published:
                return redirect('home')
            return redirect('home_out')
    else:
        form = BLogForms()
    context = {
        'form': form
    }

    return render(request, 'blog/create.html', context=context)


def delete(request, blog_id,):
    blog = get_object_or_404(Blog, id=blog_id,author=request.user)
    blog.delete()
    return redirect('home')
