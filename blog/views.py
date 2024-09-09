from django.shortcuts import render, redirect
from .models import BlogPost
from django.utils import timezone

def post_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            BlogPost.objects.create(title=title, content=content, pub_date=timezone.now())
        return redirect('post_list')
    
    posts = BlogPost.objects.order_by('-pub_date')
    return render(request, 'blog/post_list.html', {'posts': posts})