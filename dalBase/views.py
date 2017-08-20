
from django.shortcuts import render, redirect
from rest_framework import generics
from .serializers import IncidentSerializer, UnderWaySerializer, UnderWaySerializerPOST
from .models import Incident, UnderWay, User
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'index.html', content_type='text/html')


@login_required(login_url='/dalBase/login/')
def profile(request):
    user = ''
    if request.user.is_authenticated:
        user = request.user
        args: {'user': user}
        return render(request, 'parts/profile.html', args, content_type='text/html')
    return render(request, 'index.html', content_type='text/html')    
# API VIEWS


class IncidentsApiView(generics.ListCreateAPIView):
    """This class defines the create behavior of Incident Api."""
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new incident."""
        serializer.save()


class LastIncidentApiView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Incident.objects.order_by('created_at')[:1]
    serializer_class = IncidentSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new incident."""
        serializer.save()


class UnderWayApiView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    # active = Incident.objects.latest('created_at').pk
    active = 1
    # queryset = UnderWay.objects.all().filter(incident=active).telephone_set.all()
    queryset = UnderWay.objects.select_related('telephone').filter(incident=active).all()
    # queryset = list(itertools.chain(Tweet.objects.all(), Article.objects.all()))
    # The following two rows might work if applied through a serializer that understands what I want to do.
    # phonenumbers = Incident.objects.get(id=active).underway_set.all()
    # queryset = User.objects.all().filter(primary_phone__in=[phonenumbers])

    # queryset = User.objects.all().filter(primaryphone=phonenumbers.telephone)
    # queryset = Incident.objects.get(id=active).underway_set.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UnderWaySerializerPOST
        return UnderWaySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new incident."""
        serializer.save()

