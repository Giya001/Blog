from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import BLogForms
from blog.models import Blog


def home(request):
    context = {
        'blogs': Blog.objects.all()
    }
    return render(request, 'blog/home.html', context=context)


def detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/detail.html', context=context)


def update(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = BLogForms(request.POST, request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BLogForms(instance=blog)

    return render(request, 'blog/update.html', {'form': form, 'blog': blog})
