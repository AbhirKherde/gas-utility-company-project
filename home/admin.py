from django.contrib import admin
from home.models import subrequest
from home.models import Profile
from home.models import ServiceRequest
# Register your models here.
admin.site.register(subrequest)

admin.site.register(Profile)
admin.site.register(ServiceRequest)