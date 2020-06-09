from django.conf.urls import  url
from . import views



MonetaryUrlPatterns = [
    url(r'^monetary/$', views.MonetaryViewSet.as_view({'get': 'list'}), name='monetary'),
]