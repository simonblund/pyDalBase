from django import forms
from .models import IncidentReport

class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = IncidentReport
        fields = ('incident_id', 'incident_type', 'incident_type_of_alarm')
