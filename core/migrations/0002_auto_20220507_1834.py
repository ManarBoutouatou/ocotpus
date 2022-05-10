# Generated by Django 3.2.10 on 2022-05-07 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.category', verbose_name='DAS categorie'),
        ),
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.CharField(max_length=100, verbose_name='nom de l icon du site https://fontawesome.com/icons'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.TextField(blank=True, null=True, verbose_name='Petit text'),
        ),
    ]
