# Generated by Django 3.1.3 on 2020-12-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20201218_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='chest',
            name='image',
            field=models.ImageField(default='', upload_to='media/image'),
        ),
        migrations.AddField(
            model_name='dining',
            name='image',
            field=models.ImageField(default='', upload_to='media/image'),
        ),
        migrations.AddField(
            model_name='dressing',
            name='image',
            field=models.ImageField(default='', upload_to='media/image'),
        ),
        migrations.AddField(
            model_name='wardrobs',
            name='image',
            field=models.ImageField(default='', upload_to='media/image'),
        ),
    ]