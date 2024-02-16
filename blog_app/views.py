from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse
from .models import Post, Category

def blog_page(request):
    posts = Post.objects.all()
    physics_post = Post.objects.filter(category__slug__contains='physics')[:3][::-1]
    chemistry_post = Post.objects.filter(category__slug__contains='chemistry')[:3][::-1]
    math_post = Post.objects.filter(category__slug__contains='math')[:3][::-1]
    return render(request, 'blog_app/blog_page.html', {'posts':posts,'physics':physics_post, 'chemistry':chemistry_post, 'math':math_post,})


def blog_post(request, slug):
    posts = Post.objects.filter(slug =slug)

    all_posts = Post.objects.all()[:4][::-1]
    if posts:
        return render(request  , 'blog_app/blog_post.html' , {'post' : posts.first(), 'all_posts':all_posts})
    else:
        return redirect('blog_app/blog_page.html')

def blog_post_category (request, slug):
    category= Category.objects.filter(slug=slug).first()
    if not category:
        return redirect('blog_app/blog_page.html')
    posts = Post.objects.filter(category =category)
    if posts:
        return render(request  , 'blog_app/post_category.html' , {'posts' : posts,'category':slug})
    else:
        return redirect('blog_app/blog_page.html')