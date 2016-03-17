"""instablog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login as django_login
from django.contrib.auth.views import logout as django_logout
from django.conf import settings

from blog import views as blog_views

urlpatterns = [
    url(r'^posts/create/$',blog_views.create_post, name="create_post" ),
    url(r'^$',blog_views.list_posts, name="list_posts"), #^뒤에 있는걸로 시작한다.  $는 이걸로 끝난다 라는 뜻. 
    url(r'^hello/$',blog_views.hello2),
    url(r'^view_post/(?P<pk>[0-9]+)/$',blog_views.view_post ,name='view_post'),
    url(r'^delete_post/(?P<pk>[0-9]+)/$',blog_views.delete_post, name='delete_post'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', django_login,{'template_name':'login.html'},name='login_url'),
    url(r'^logout/$', django_logout,{'next_page':'settings.LOGIN_URL'}, name='logout_url'),

]
