# Generated by Django 4.2.4 on 2023-10-11 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='amount_in_stock',
        ),
    ]