# Generated by Django 3.2.9 on 2021-12-01 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20211130_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='banners',
            name='title',
            field=models.CharField(default=4.123371268349002e-05, max_length=75, verbose_name='Título'),
            preserve_default=False,
        ),
    ]
