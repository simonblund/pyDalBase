from django.conf.urls import url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import IncidentsApiView, LastIncidentApiView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    url(r'^api/v1/incidents$', IncidentsApiView.as_view(), name="create"),
    url(r'^api/v1/incident$', LastIncidentApiView.as_view(), name="create"),
]

urlpatterns = format_suffix_patterns(urlpatterns)