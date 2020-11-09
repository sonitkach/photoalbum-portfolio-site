from django import forms
from django.forms import ModelForm

from .models import Post, PostImage

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }


"""class PostImageForm(ModelForm):
    class Meta:
        model = PostImage
        extra = 1
        max_num = 10
        fields = ('images',)
        #exclude = ('post',)"""