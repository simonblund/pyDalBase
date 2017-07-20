from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import IncidentSerializer
from .models import Incident
# Create your views here.


def index(request):
    return render(request, 'index.html', content_type='text/html')


class IncidentsApiView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new incident."""
        serializer.save()


class LastIncidentApiView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = [Incident.objects.order_by('created_at')[0]]
    serializer_class = IncidentSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new incident."""
        serializer.save()