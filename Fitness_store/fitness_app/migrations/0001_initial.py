# Generated by Django 4.2.4 on 2023-09-07 08:48

import Fitness_store.fitness_app.models
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='GymEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('description', models.TextField(max_length=300, validators=[django.core.validators.MinLengthValidator(5)])),
                ('best_selling', models.BooleanField(default=False)),
                ('price', models.FloatField()),
                ('photo', models.FileField(default=None, upload_to='gym_equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Supplements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('description', models.TextField(max_length=300, validators=[django.core.validators.MinLengthValidator(5)])),
                ('best_selling', models.BooleanField(default=False)),
                ('amount', models.IntegerField()),
                ('amount_type', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('photo', models.FileField(default=None, upload_to='supplements')),
            ],
        ),
        migrations.CreateModel(
            name='FitnessUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), Fitness_store.fitness_app.models.validate_only_alphabetical])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), Fitness_store.fitness_app.models.validate_only_alphabetical])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('profile_picture', models.FileField(blank=True, default=None, null=True, upload_to='profile_pictures')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]