# Generated by Django 4.2.4 on 2023-11-06 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='product_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
