# Generated by Django 3.2.10 on 2022-05-07 21:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_service_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='aperçu',
            field=models.CharField(default=django.utils.timezone.now, max_length=300, verbose_name='aperçu'),
            preserve_default=False,
        ),
    ]
