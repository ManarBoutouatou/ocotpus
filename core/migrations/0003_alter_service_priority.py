# Generated by Django 3.2.10 on 2022-05-07 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220507_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='priority',
            field=models.IntegerField(blank=True, null=True, verbose_name='ordre / priorité'),
        ),
    ]
