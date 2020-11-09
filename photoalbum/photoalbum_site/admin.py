from django.contrib import admin

from .models import Post,Tag,PostImage


class PostImageAdmin(admin.StackedInline):
    model = PostImage

class TagAdmin(admin.StackedInline):
    model = Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Post


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


#admin.site.register (Post)
#admin.site.register (Tag)
#admin.site.register (PostImage)
from django.contrib import admin

# Register your models here.
