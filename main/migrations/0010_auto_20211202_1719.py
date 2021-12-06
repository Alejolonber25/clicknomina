# Generated by Django 3.2.9 on 2021-12-02 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_banners_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='why',
            field=models.TextField(verbose_name='Por qué nuestros clientes confían en CLICKNÓMINA'),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]