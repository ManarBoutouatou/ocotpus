# Generated by Django 3.2.10 on 2022-05-23 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_status_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.service'),
        ),
    ]
