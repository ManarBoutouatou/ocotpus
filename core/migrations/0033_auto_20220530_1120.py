# Generated by Django 3.2.10 on 2022-05-30 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20220530_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offre',
            old_name='prix',
            new_name='price_month',
        ),
        migrations.AddField(
            model_name='offre',
            name='price_year',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True),
        ),
    ]