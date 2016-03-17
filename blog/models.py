from django.db import models
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    tags = models.ManyToManyField('Tag')# 문자열로 연결하면 모델을 전부 다 읽고 나서 나중에 평가해서 관계를 맺어준다. app_name.Tag 라고 하면 다른 앱에있는거 가져온다.
    category = models.ForeignKey('Category', null=True)
    #### 모델의 기본적인 형태####
    title = models.CharField(max_length=200) #255이하 글자를 입력할 수 있는 데이터베이스 컬럼이 charField
    content = models.TextField()#디비마다 다르지만 통산적으로 글자수에 제약이 없다.
    created_at = models.DateTimeField(auto_now_add=True)#처음데이터가 만들어 질때 생성일시가 자동으로 들어가도록
    updated_at = models.DateTimeField(auto_now=True)#수정이 될 때 마다 자동으로 수정일시가 들어간다.
    ########################

    #models 필드로 만들어진 부분만 장고에서 인식하고 디비의 컬럼으로 만든다.
    is_model_field = False # 파이썬 코드로만 존재하고 컬럼으로는 만들어 지지 않는다.

    def __str__(self):
        return '{}-{}'.format(self.pk,self.title)


    class Meta:
        ordering = ('-updated_at', '-pk',)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} of {}'.format(self.pk, self.post.pk)

class Tag(models.Model):
    name = models.CharField(max_length=40)

class Category(models.Model):
    name = models.CharField(max_length=40)