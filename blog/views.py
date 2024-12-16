from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator

def blogs(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'blogs': blogs,
        'page_obj': page_obj,
    }
    return render(request, 'blog/blogs.html', context)


def blog_detail(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    context = {
        'blog': blog
    }
    return render(request, 'blog/blog-details.html', context)