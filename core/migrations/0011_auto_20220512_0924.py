# Generated by Django 3.2.10 on 2022-05-12 08:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_pagetitle'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ('id',), 'verbose_name': 'portfolio', 'verbose_name_plural': 'portfolios'},
        ),
        migrations.AddField(
            model_name='category',
            name='actif',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de Création'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour'),
        ),
        migrations.AddField(
            model_name='client',
            name='actif',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='client',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de Création'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour'),
        ),
        migrations.AddField(
            model_name='pagetitle',
            name='actif',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de Création'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour'),
        ),
        migrations.AddField(
            model_name='service',
            name='actif',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='service',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de Création'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour'),
        ),
        migrations.AddField(
            model_name='solution',
            name='actif',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de Création'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solution',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to='images/prtfolio'),
        ),
    ]
