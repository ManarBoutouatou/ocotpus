# Generated by Django 3.2.10 on 2022-05-23 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20220523_0931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offre',
            name='service',
        ),
        migrations.AddField(
            model_name='fonctionalite',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.service'),
        ),
    ]
