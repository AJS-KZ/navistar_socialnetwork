from django.contrib import admin

from posts.models import Post, PostLike


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    pass
