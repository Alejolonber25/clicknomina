# Generated by Django 3.2.9 on 2021-11-30 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211129_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modification_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('elimination_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('image', models.ImageField(upload_to='banner/', verbose_name='Imágen')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modification_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('elimination_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('experience', models.IntegerField(max_length=3, verbose_name='Años de Experiencia')),
                ('why', models.TextField(verbose_name='Por qué confían en CLICKNÓMINA')),
                ('trayectory', models.TextField(verbose_name='Conoce nuestra trayectoria')),
                ('commitment', models.TextField(verbose_name='Nuestro Compromiso')),
                ('mission', models.TextField(verbose_name='Misión')),
                ('vision', models.TextField(verbose_name='Visión')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('image_01', models.ImageField(upload_to='empresa/', verbose_name='Imágen 1')),
                ('image_02', models.ImageField(upload_to='empresa/', verbose_name='Imágen 2')),
                ('image_03', models.ImageField(upload_to='empresa/', verbose_name='Imágen 3')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
