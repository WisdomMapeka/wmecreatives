# Generated by Django 3.1.12 on 2021-07-05 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20210701_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='styleshit',
            field=models.CharField(blank=True, choices=[('one', 'one'), ('one', 'one'), ('one', 'one'), ('one', 'one')], max_length=100, null=True),
        ),
    ]
