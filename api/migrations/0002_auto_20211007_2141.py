# Generated by Django 3.0.8 on 2021-10-07 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='nickname',
        ),
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.TextField(blank=True),
        ),
    ]