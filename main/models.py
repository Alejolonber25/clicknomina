

from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from clicknomina.utils import unique_slug_generator
from clicknomina.utils import slugify


class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado', default=True)
    creation_date = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    modification_date = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)
    elimination_date = models.DateField('Fecha de Eliminación', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Contacts(ModeloBase):
    name = models.CharField('Nombre', max_length=120)
    email = models.CharField('Correo Electrónico', max_length=120)
    cel = models.CharField('Número de Contacto', max_length=18)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.email

class Posts(ModeloBase):
    title = models.CharField('Título', max_length=150, unique=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    content = RichTextField()
    image = models.ImageField('Imágen', upload_to='servicio/')

    class Meta:
        abstract = True


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


class Business(ModeloBase):
    experience = models.IntegerField('Años de Experiencia')
    why = models.TextField('Por qué nuestros clientes confían en CLICKNÓMINA')
    trayectory = models.TextField('Conoce nuestra trayectoria')
    commitment = models.TextField('Nuestro Compromiso')
    mission = models.TextField('Misión')
    vision = models.TextField('Visión')
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    image_01 = models.ImageField('Imágen 1', null=True, upload_to='empresa/')
    image_02 = models.ImageField('Imágen 2', null=True, upload_to='empresa/')

    class Meta:
        verbose_name = 'Información de la Empresa'
        verbose_name_plural = 'Información de la empresa'

    def __str__(self):
        return "{0} años de experiencia".format(self.experience)


class Banners(ModeloBase):
    title = models.CharField('Título', max_length=75)
    image = models.ImageField('Imágen', upload_to='banner/')

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return "{0}".format(self.id)


class Services(Posts):

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.title


class News(Posts):

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.title


pre_save.connect(slug_generator, sender=Services)
pre_save.connect(slug_generator, sender=News)
