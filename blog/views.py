from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger # 숫자가 아닐경우
from django.core.paginator import EmptyPage #빈 값일 경우 

from .models import Post
from .models import Category
from .models import Comment

def hello(request):
    res = HttpResponse('hello world')
    return res

def hello2(request):
    return render(request, 'hello.html')

def list_posts(request):
    per_page = 3
    current_page = request.GET.get('page',1)

    all_posts = Post.objects.select_related().all().order_by('pk')#select_related() 1:다로 연결되어 있으면 조인을 해서 한번에 들고 온다.
    

    pagi = Paginator(all_posts, per_page)
    try:
        pg = pagi.page(current_page)
    except PageNotAnInteger:
        pg = pagi.page(1)
    except EmptyPage:
        pg = []

    return render(request, 'list_posts.html',{
        'posts': pg,
    })

def view_post(request,pk):
    if request.method == 'POST':
        new_comment = Comment()
        new_comment.content = request.POST.get('content')

        print(new_comment.content)
        the_post = get_object_or_404(Post,pk=pk)
        new_comment.post = the_post
        
        new_comment.save()
        
        print('view_post')
    the_post = get_object_or_404(Post,pk=pk)
    #the_post = Post.objects.get(pk=pk)

    return render(request, 'view_post.html',{
        'post': the_post
    })

def add_comment(request):
    print('add_comment')
    if request.method == 'POST':
        new_comment = Comment()
        new_comment.content = request.POST.get('content')

        post_id = request.POST.get('post_id')
        the_post = get_object_or_404(Post,pk=post_id)
        new_comment.post = the_post
        new_comment.save()

    return redirect('view_post',pk=post_id)

def delete_comment(request):
    print('delete_comment')
    if request.method == 'POST':
        new_comment = Comment()
        new_comment.id = request.POST.get('comment_id')

        print(new_comment.id)

        post_id = request.POST.get('post_id')
        the_post = get_object_or_404(Post,pk=post_id)

        new_comment.delete()

    return redirect('view_post',pk=post_id)


def create_post(request):
    categories = Category.objects.all()

    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        new_post = Post()
        new_post.title = request.POST.get('title')
        new_post.content = request.POST.get('content')
        # new_post.title = request.POST.get('title')

        print(request.POST)
        category_pk = request.POST.get('category')
        print(category_pk)
        category = get_object_or_404(Category,pk=category_pk)
        new_post.category = category
        new_post.save()

        return redirect('view_post',pk=new_post.pk)



    
    return render(request, 'create_post.html',{
        'categories':categories,
    })







