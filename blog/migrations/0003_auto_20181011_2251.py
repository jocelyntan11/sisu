# Generated by Django 2.0.5 on 2018-10-11 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181011_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hitcount',
            name='url_hit',
        ),
        migrations.DeleteModel(
            name='HitCount',
        ),
        migrations.DeleteModel(
            name='UrlHit',
        ),
    ]
