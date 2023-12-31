# Generated by Django 4.2.3 on 2023-08-07 15:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password1', models.CharField(default='password1', max_length=30)),
                ('password2', models.CharField(default='password2', max_length=30)),
                ('name', models.CharField(default='name', max_length=30)),
                ('nickname', models.CharField(default='nickname', max_length=30, null=True)),
                ('phone', models.CharField(default='phone', max_length=100)),
                ('birthday', models.CharField(default='birthday', max_length=30)),
                ('address1', models.CharField(default='address1', max_length=255)),
                ('address2', models.CharField(default='address2', max_length=255)),
                ('address3', models.CharField(default='address3', max_length=255)),
                ('usertype', models.CharField(default='usertype', max_length=255)),
                ('profile', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
