# Generated by Django 3.2.10 on 2022-05-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20220525_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fonctionalite',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offre',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
