# Generated by Django 3.2.10 on 2022-05-12 09:01

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20220512_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='pricing',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Déscription du produit'),
        ),
    ]