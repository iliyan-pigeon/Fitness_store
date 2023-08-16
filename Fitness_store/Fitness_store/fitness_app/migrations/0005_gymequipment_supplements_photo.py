# Generated by Django 4.2.4 on 2023-08-14 18:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0004_supplements'),
    ]

    operations = [
        migrations.CreateModel(
            name='GymEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('price', models.FloatField()),
                ('photo', models.FileField(default=None, upload_to='gym_equipment')),
            ],
        ),
        migrations.AddField(
            model_name='supplements',
            name='photo',
            field=models.FileField(default=None, upload_to='supplements'),
        ),
    ]