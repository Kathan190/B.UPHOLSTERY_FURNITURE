# Generated by Django 3.0.5 on 2020-12-16 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sofa',
            name='digital',
        ),
    ]
