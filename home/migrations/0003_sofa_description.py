# Generated by Django 3.0.5 on 2020-12-16 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_sofa_digital'),
    ]

    operations = [
        migrations.AddField(
            model_name='sofa',
            name='description',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
