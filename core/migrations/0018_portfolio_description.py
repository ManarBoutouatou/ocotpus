# Generated by Django 3.2.10 on 2022-05-17 15:38

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_portfolio_texte_haut'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='description '),
        ),
    ]
