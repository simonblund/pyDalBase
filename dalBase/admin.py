from django.contrib import admin


from .models import User, UnderWay, Incident

admin.site.register(User)
admin.site.register(Incident)
admin.site.register(UnderWay)


