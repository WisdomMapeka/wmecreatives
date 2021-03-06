# Generated by Django 3.1.2 on 2021-04-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210410_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='inner_background_img',
            field=models.ImageField(blank=True, null=True, upload_to='media_files/homepage/background_img/inner'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='outer_background_img',
            field=models.ImageField(blank=True, null=True, upload_to='media_files/homepage/background_img/outer'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='language',
            field=models.CharField(blank=True, choices=[('python', 'python'), ('javascript', 'javascript'), ('django', 'django'), ('css', 'css'), ('html', 'html'), ('mysql', 'mysql'), ('postgresql', 'postgresql')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media_files/homepage/background_video'),
        ),
    ]
