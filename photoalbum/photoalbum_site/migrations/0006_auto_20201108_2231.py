# Generated by Django 3.1 on 2020-11-08 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoalbum_site', '0005_postimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='images',
            field=models.ImageField(upload_to='images'),
        ),
    ]