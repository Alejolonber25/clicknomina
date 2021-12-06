from django.urls import path

from .views import *


urlpatterns = [
    path('', PageIndex.as_view(), name='index'),
    path('contact', Contact, name='contact'),
    path('blog/', PageBlog.as_view(), name='blog'),
    path('blog/<slug:slug>', PageNew.as_view(), name="new"),
    path('services/', PageServices.as_view(), name="services"),
    path('service/<slug:slug>', PageService.as_view(), name="service"),
]
