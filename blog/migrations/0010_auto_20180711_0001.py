# Generated by Django 2.0.5 on 2018-07-10 23:01

import blog.models
from django.db import migrations
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180627_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category_name',
            field=enumfields.fields.EnumField(default='Harassment', enum=blog.models.Category, max_length=200),
        ),
    ]
