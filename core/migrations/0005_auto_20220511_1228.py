# Generated by Django 3.2.10 on 2022-05-11 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_article_aperçu'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/services', verbose_name='img 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='section',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='section to show'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/services', verbose_name='img 1'),
            preserve_default=False,
        ),
    ]
