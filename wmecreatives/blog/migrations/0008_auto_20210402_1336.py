# Generated by Django 3.1.2 on 2021-04-02 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_youtubevideos'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubevideos',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='youtubevideos',
            name='title',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
