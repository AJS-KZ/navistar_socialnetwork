from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from posts.models import Post, PostLike


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = (
            'uuid',
            'title',
            'text',
            'author'
        )


class PostLikeSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PostLike
        fields = (
            'owner',
            'like',
            'date'
        )

    def validate(self, attrs):
        kwargs = self.context['kwargs']
        pk = kwargs['pk']
        post = get_object_or_404(Post, pk=pk)

        if post:
            attrs['post'] = post
        else:
            raise ValidationError('Post not found!')

        return attrs
