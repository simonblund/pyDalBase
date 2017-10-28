
from rest_framework import serializers
from .models import Incident, UnderWay, User, IncidentReport
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
        model = User
        fields = ('id', 'first_name', 'last_name', 'is_staff',
                  'vacancy')


class UnderWaySerializer(serializers.ModelSerializer):
    incident = serializers.PrimaryKeyRelatedField(queryset=Incident.objects.all())
    telephone = UserSerializer(many=False, read_only=False)

    class Meta:
        model = UnderWay
        fields = ('id', 'incident', 'time', 'telephone', 'created_at')
        read_only_fields = ('created_at', 'id')


class UnderWaySerializerPOST(serializers.ModelSerializer):

    class Meta:
        model = UnderWay
        fields = ('id', 'incident', 'time', 'telephone')
        read_only_fields = ('created_at', 'id')


class IncidentReportserializer(serializers.ModelSerializer):

    class Meta:
        model = IncidentReport
        fields = ('id', 'incident_id',
                  'incident_type', 'incident_type_of_alarm', 'incident_message',
                  'incident_address', 'incident_area', 'incident_city', 'incident_detail',
                  'description', 'confirmed_fire', 'action_taken', 'incident_cause', 'users_on_incident',
                  'active_users', 'start_time_date', 'end_time_date', 'image_1',
                  'image_2', 'image_3')
        read_only_fields = ('created_at', 'id')



