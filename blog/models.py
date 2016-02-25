from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.name)
        
class Post(models.Model):
    category = models.ForeignKey(Category, null=True)
    tag = models.ManyToManyField('Tag') #모델 클래스의 이름을 인자로 전달
    title = models.CharField(max_length=255) #CharField는 max_length가 필수로 있어야 한다.
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add는 생성될 때 자동으로 입력된다.
    updated_at = models.DateTimeField(auto_now=True) # auto_now는 수정될 때 시간이 입력된다.

    is_model_field = False

    def __str__(self):
        return '{}-{}'.format(self.pk,self.title)

class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.created_at,self.content)

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.name)


