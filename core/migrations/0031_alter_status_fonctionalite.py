# Generated by Django 3.2.10 on 2022-05-25 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20220525_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='fonctionalite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status', to='core.fonctionalite', verbose_name='fonctionalite'),
        ),
    ]