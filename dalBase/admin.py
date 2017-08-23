from django.contrib import admin


from .models import User, UnderWay, Incident, IncidentType, IncidentCause, IncidentArea, Vehicle, VehicleUnderWay, IncidentReport

admin.site.register(User)
admin.site.register(Incident)
admin.site.register(UnderWay)
admin.site.register(IncidentType)
admin.site.register(IncidentCause)
admin.site.register(IncidentArea)
admin.site.register(Vehicle)
admin.site.register(VehicleUnderWay)
admin.site.register(IncidentReport)



