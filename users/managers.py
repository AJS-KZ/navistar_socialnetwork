from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def _create_user(self, phone, password, is_staff, is_superuser, **extra_fields):
        if not phone:
            raise ValueError(_('users.custom_user_manager.value_error.not_phone'))
        user = self.model(
            phone=phone,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        # Check if password has been given
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    # Change following functions signature to allow "No password"
    def create_user(self, phone, password=None, **extra_fields):
        return self._create_user(phone, password, False, False, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('users.custom_user_manager.value_error.not_staff'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('users.custom_user_manager.value_error.not_superuser'))
        return self._create_user(phone, password, **extra_fields)
