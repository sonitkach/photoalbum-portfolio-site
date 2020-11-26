from django import forms
from django.forms import ModelForm

from .models import Post, PostImage

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'tags': forms.CheckboxSelectMultiple,
            'featured': forms.CheckboxInput,
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
        self.fields['tags'].widget.attrs['height'] = 100
        #self.fields['long_desc'].widget.attrs['rows'] = 20


"""class PostImageForm(ModelForm):
    class Meta:
        model = PostImage
        extra = 1
        max_num = 10
        fields = ('images',)
        #exclude = ('post',)"""