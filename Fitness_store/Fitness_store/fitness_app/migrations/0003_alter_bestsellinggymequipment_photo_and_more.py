# Generated by Django 4.2.4 on 2023-08-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0002_alter_bestsellinggymequipment_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestsellinggymequipment',
            name='photo',
            field=models.FileField(upload_to='best_products_images'),
        ),
        migrations.AlterField(
            model_name='bestsellingsupplements',
            name='photo',
            field=models.FileField(upload_to='best_products_images'),
        ),
    ]