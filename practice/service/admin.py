from django.contrib import admin
from service.models import service

class ServiceAdmin(admin.ModelAdmin):
    list_display= ('username', 'password')

admin.site.register(service, ServiceAdmin)
# Register your models here.
