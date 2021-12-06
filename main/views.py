from django.core.mail.message import EmailMultiAlternatives
from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .models import Business, Banners, Services, News, Contacts
from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from django.contrib import messages
from clicknomina import settings

class PageIndex(ListView):
    def get(self, request, *args, **kwargs):
        banners = Banners.objects.filter(
            state=True
        )
        services = Services.objects.filter(
            state=True
        )
        news_top = News.objects.filter(state=True).count()
        if news_top <= 2:
            news_top = 0
        else:
            news_top -= 3
        news = News.objects.filter(state=True)[news_top:]
        business = Business.objects.filter(
            state=True
        )[0]
        context = {
            'services': services,
            'news': news,
            'business': business,
            'banners': banners,
        }
        return render(request, 'index.html', context)


def Contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        cel = request.POST['cel']
        content = request.POST['content']
        context = {
            'name': name,
            'email': email,
            'cel': cel,
            'content': content,
        }
        contact = Contacts(name=name, email=email, cel=cel)
        contact.save()
        template = get_template('email_template.html')
        body = template.render(context)
        email = EmailMultiAlternatives('Información de Contacto', 'Información de Contacto', settings.EMAIL_HOST_USER, ['info.clicknomina@gmail.com'],)
        email.attach_alternative(body, 'text/html')
        email.fail_silently = False
        email.send()
        
        messages.success(request, 'tu información de contacto ha sido enviada, pronto te contactaremos :)')
    else:
        messages.success(request, 'surgió un error al tratar de enviar el contacto')
    return redirect('main:index')

class PageServices(ListView):
    def get(self, request, *args, **kwargs):
        services = Services.objects.filter(
            state=True
        )
        context = {
            'services': services,
            'route': 'services'
        }
        return render(request, 'services.html', context)


class PageBlog(ListView):
    def get(self, request, *args, **kwargs):
        news = News.objects.filter(
            state=True
        )
        context = {
            'news': news,
        }
        return render(request, 'blog.html', context)


class PageService(DetailView):
    def get(self, request, slug, *args, **kwargs):
        try:
            service = Services.objects.get(slug=slug)
        except:
            service = None
        context = {
            'service': service,
        }
        return render(request, 'service.html', context)


class PageNew(DetailView):
    def get(self, request, slug, *args, **kwargs):
        try:
            new = News.objects.get(slug=slug)
        except:
            new = None
        context = {
            'new': new,
        }
        return render(request, 'new.html', context)
