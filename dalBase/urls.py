
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.views import login
from django.conf import settings
from django.conf.urls.static import static

from .views import IncidentsApiView, LastIncidentApiView, UnderWayApiView, IncidentReportViewSet, UserView

from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('testincidents', IncidentReportViewSet, base_name='testincidents')

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),

    url(r'^api/v1/', include(router.urls)),

    url(r'^login/$', login, {'template_name': 'dalbase/login.html'}),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^reports/$', views.reports, name='reports'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    url(r'^api/v1/user$', UserView.as_view(), name="create"),
    url(r'^api/v1/incidents$', IncidentsApiView.as_view(), name="create"),
    url(r'^api/v1/incident$', LastIncidentApiView.as_view(), name="create"),
    url(r'^api/v1/underway$', UnderWayApiView.as_view(), name="create"),
    # url(r'^api/v1/incidentreport$', IncidentReportApiView.as_view(), name="get_all"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
