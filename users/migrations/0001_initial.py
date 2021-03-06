# Generated by Django 3.2.6 on 2021-08-22 14:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='utils.base_model.uuid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='utils.model_date.created_at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='utils.model_date.updated_at')),
                ('phone', models.CharField(max_length=15, unique=True, verbose_name='Моб.номер тел.')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Эл.адрес')),
                ('password', models.CharField(blank=True, max_length=128, null=True, verbose_name='password')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия')),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=6, null=True, verbose_name='Пол')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='uploads/avatars/', verbose_name='Аватар')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('last_activity', models.DateTimeField(blank=True, null=True, verbose_name='last activity')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ('updated_at',),
            },
        ),
    ]
