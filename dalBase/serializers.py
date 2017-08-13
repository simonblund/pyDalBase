
from rest_framework import serializers
from .models import Incident, UnderWay, User
import logging
logger = logging.getLogger(__name__)


class IncidentSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Incident
        fields = ('id', 'active', 'message',
                  'address', 'pos_lon', 'pos_lan',
                  'type', 'area', 'details', 'time',
                  'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields = ('id', 'first_name', 'last_name', 'competences', 'driverslicence',
                  'vacancy')


class UnderWaySerializer(serializers.ModelSerializer):
    incident = serializers.PrimaryKeyRelatedField(queryset=Incident.objects.all())
    telephone = UserSerializer(many=False, read_only=False)

    class Meta:
        model = UnderWay
        fields = ('id', 'incident', 'time', 'telephone')
        read_only_fields = ('created_at', 'id')


class UnderWaySerializerPOST(serializers.ModelSerializer):

    class Meta:
        model = UnderWay
        fields = ('id', 'incident', 'time', 'telephone')
        read_only_fields = ('created_at', 'id')




