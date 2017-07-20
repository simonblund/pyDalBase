from rest_framework import serializers
from .models import Incident

class IncidentSerializer(serializers.ModelSerializer):


    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Incident
        fields = ('id', 'active', 'message',
                  'address', 'pos_lon', 'pos_lan',
                  'type', 'area', 'details', 'time',
                  'created_at', 'updated_at')
        read_only_fields = ('created_at', 'created_at')