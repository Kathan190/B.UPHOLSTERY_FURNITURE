# Generated by Django 3.0.5 on 2020-12-16 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_sofa_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sofa',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
