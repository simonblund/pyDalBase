
from rest_framework import serializers
from .models import Incident, UnderWay, User, IncidentReport, IncidentType, IncidentArea, IncidentCause
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


class IncidentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentType
        fields = ('id', 'incident_type')


class IncidentAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentArea
        fields = ('id', 'incident_area_no', 'incident_area_name')


class IncidentCauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentCause
        fields = ('id', 'incident_cause')


class ShortUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'vacancy', 'last_name')


class ShortIncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ('id', 'pos_lon', 'pos_lan', 'created_at')

class IncidentReportListSerializer(serializers.ModelSerializer):
    incident_type = IncidentTypeSerializer(many=False, read_only=False)

    class Meta:
        model = IncidentReport
        fields = ('id', 'incident_id', 'incident_type', 'confirmed_fire', 'start_time_date')


class IncidentReportRetrieveSerializer(serializers.ModelSerializer):
    incident_type = IncidentTypeSerializer(many=False, read_only=False)
    incident_area = IncidentAreaSerializer(many=False, read_only=False)
    incident_cause = IncidentCauseSerializer(many=False, read_only=False)
    users_on_incident = ShortUserSerializer(many=True, read_only=True)
    incident_id = ShortIncidentSerializer(many=False, read_only=True)

    class Meta:
        model = IncidentReport
        fields = ('id', 'incident_id',
                  'incident_type', 'incident_type_of_alarm', 'incident_message',
                  'incident_address', 'incident_area', 'incident_city', 'incident_detail',
                  'description', 'confirmed_fire', 'action_taken', 'incident_cause', 'users_on_incident',
                  'active_users', 'start_time_date', 'end_time_date', 'image_1',
                  'image_2', 'image_3')
        read_only_fields = ('created_at', 'id')



