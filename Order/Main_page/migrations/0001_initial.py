# Generated by Django 4.2.5 on 2023-10-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('screen', models.CharField(max_length=255)),
                ('camera', models.CharField(max_length=255)),
                ('memory', models.CharField(max_length=255)),
                ('cpu', models.CharField(max_length=255)),
                ('case', models.CharField(max_length=255)),
                ('image_path', models.CharField(max_length=255)),
            ],
        ),
    ]
