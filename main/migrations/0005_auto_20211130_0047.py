# Generated by Django 3.2.9 on 2021-11-30 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_banner_business'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': 'Banner', 'verbose_name_plural': 'Banners'},
        ),
        migrations.AlterModelOptions(
            name='business',
            options={'verbose_name': 'Información de la Empresa', 'verbose_name_plural': 'Informaciónd e la empresa'},
        ),
    ]
