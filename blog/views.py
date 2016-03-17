from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger # 숫자가 아닐경우
from django.core.paginator import EmptyPage #빈 값일 경우 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import PermissionDenied

from .models import Post
from .models import Category
from .forms import PostForm
from .forms import PostEditForm
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
    the_post = get_object_or_404(Post,pk=pk)
    #the_post = Post.objects.get(pk=pk)

    return render(request, 'view_post.html',{
        'post': the_post
    })

@login_required
# @permission_required('blog.delete_post',raise_exception=True)
def delete_post(request,pk):
    the_post = get_object_or_404(Post,pk=pk)
    if request.user.id != the_post.user.id:
        raise PermissionDenied
    if request.method == 'POST':
        the_post.delete()    
        return redirect('list_posts')

    return render(request, 'view_post.html',{
        'post': the_post
    })

@login_required
def create_post(request):
    categories = Category.objects.all()

    if request.method == 'GET':
        form = PostEditForm()

    elif request.method == 'POST':
        form = PostEditForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            
            return redirect('view_post',pk=new_post.pk)

    return render(request, 'create_post.html',{
        'categories':categories,
        'form':form,
    })







