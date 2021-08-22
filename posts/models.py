from django.db import models

from utils.models import AbstractUUID, AbstractTimeTracker
from utils.const import LikeDislikeChoice
from users.models import CustomUser


class Post(AbstractUUID, AbstractTimeTracker):
    title = models.CharField(
        max_length=512,
        verbose_name='Наименование поста'
    )
    text = models.TextField(
        blank=True,
        null=True,
        verbose_name='Текст поста'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='Автор поста'
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        order_with_respect_to = 'author'

    def __str__(self):
        return self.title


class PostLike(AbstractUUID, AbstractTimeTracker):
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост',
        related_name='likes_dislikes'
    )
    like = models.CharField(
        max_length=7,
        choices=LikeDislikeChoice.choices(),
        verbose_name='Like-Dislike'
    )
    date = models.DateField(
        # auto_now=True,
        verbose_name='Дата'
    )

    class Meta:
        verbose_name = 'PostLike'
        verbose_name_plural = 'PostsLikes'
        order_with_respect_to = 'post'
