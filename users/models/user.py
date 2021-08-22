from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from users.managers import CustomUserManager
from utils.models import AbstractUUID, AbstractTimeTracker
from utils.const import GenderChoice


class CustomUser(AbstractBaseUser, PermissionsMixin, AbstractUUID, AbstractTimeTracker):
    phone = models.CharField(
        max_length=15,
        unique=True,
        verbose_name='Моб.номер тел.'
    )
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name='Эл.адрес'
    )
    password = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name=_('password')
    )
    first_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Фамилия'
    )
    gender = models.CharField(
        choices=GenderChoice.choices(),
        max_length=6,
        blank=True,
        null=True,
        verbose_name='Пол'
    )
    bio = models.TextField(
        blank=True,
        null=True,
        verbose_name='О себе'
    )
    avatar = models.ImageField(
        upload_to='uploads/avatars/',
        blank=True,
        null=True,
        verbose_name='Аватар'
    )
    is_active = models.BooleanField(
        default=True
    )
    is_staff = models.BooleanField(
        default=False
    )
    # last_login = models.DateTimeField(
    #     _('last login'),
    #     blank=True,
    #     null=True
    # )
    last_activity = models.DateTimeField(
        _('last activity'),
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'phone'

    objects = CustomUserManager()

    class Meta:
        ordering = ('updated_at', )
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f'Phone: {self.phone} | UUID: {self.uuid}'
