from django.contrib import admin

from daspf_app.models import *


class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Post)
class PostAdminAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Post


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category)
