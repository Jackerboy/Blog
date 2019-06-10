from django.shortcuts import render_to_response,get_object_or_404,render
from .models import Blog,BlogType
# Create your views here.


def blog_list(request):
    context = {}
    context['blogs']  = Blog.objects.all()
    context['blog_types'] = BlogType.objects.all()
    print(context)
    return render_to_response('blog/blog_list.html', context)



def bolg_datail(request,blog_id):
    context = {}
    context['blog'] = get_object_or_404(Blog,pk=blog_id)
    # context['blog'] = Blog.objects.get(pk=blog_id)
    return render_to_response('blog/blog_detail.html', context)


def blog_type_list(request,type_id):
    context = {}
    blog_type  = BlogType.objects.get(pk = type_id)
    # 用get返回的不是一个可迭代对象
    context['blogs'] = Blog.objects.filter(blogtype=blog_type)
    context['blog_type'] = blog_type
    context['blog_types'] = BlogType.objects.all()
    print(context)
    return render_to_response('blog/blog_type.html', context)
