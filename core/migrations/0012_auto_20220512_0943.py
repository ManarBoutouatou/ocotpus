# Generated by Django 3.2.10 on 2022-05-12 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20220512_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/services', verbose_name='img 1'),
        ),
        migrations.AlterField(
            model_name='service',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/services', verbose_name='img 2'),
        ),
    ]
