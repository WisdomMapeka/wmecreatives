# Generated by Django 3.1.12 on 2021-06-28 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20210628_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='dislikes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
