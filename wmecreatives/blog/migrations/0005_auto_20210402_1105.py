# Generated by Django 3.1.2 on 2021-04-02 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210402_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='tag',
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='blog.Tags'),
        ),
    ]
