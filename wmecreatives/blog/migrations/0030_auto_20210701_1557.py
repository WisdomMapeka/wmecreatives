# Generated by Django 3.1.12 on 2021-07-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
