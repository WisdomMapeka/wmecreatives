# Generated by Django 3.1.12 on 2021-06-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_youtubevideos_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubevideos',
            name='Tags',
            field=models.ManyToManyField(blank=True, to='blog.Tags'),
        ),
    ]
