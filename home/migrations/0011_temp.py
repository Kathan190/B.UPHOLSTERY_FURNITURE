# Generated by Django 3.0.5 on 2021-01-25 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
