from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog


# Create your views here.

def home(request):
    a = 3
    b = 4
    c = a + b
    context = {
        'a': a,
        'b': b,
        'c': c,
        'blogs': Blog.objects.all()
    }
    return render(request,'base.html',context=context)