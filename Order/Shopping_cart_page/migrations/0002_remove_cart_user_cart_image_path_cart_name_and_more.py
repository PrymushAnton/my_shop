# Generated by Django 4.2.5 on 2023-10-30 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping_cart_page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='image_path',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AddField(
            model_name='cart',
            name='name',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.CharField(default=True, max_length=255),
        ),
    ]
