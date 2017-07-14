from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]