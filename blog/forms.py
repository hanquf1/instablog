
from django import forms
from django.forms import ValidationError # exception 도 클래스

from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(required=True)
    content = forms.CharField(widget=forms.Textarea)
    

#model과 연결하는 부분. model에 post 를 연결하는 부분.
class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','category')
        #exclude = ('title','category') 이 필드는 사용하지 않겠다.
        #fields = '__all__'   전부 다 사용하겠다.

    def clean_title(self):
        title = self.cleaned_data.get('title','')
        if '바보' in title:
            raise ValidationError('바보라는 말은 쓰면 안돼요!')
        return title.strip()
       

    def clean(self):
        super(PostEditForm, self).clean()
        title = self.cleaned_data.get('title','')
        content = self.cleaned_data.get('content','')

        if '안녕' in title:
            self.add_error('title', '안녕 그만')
        if '안녕' in content:
            self.add_error('content', '안녕이라고 말하지마 ')