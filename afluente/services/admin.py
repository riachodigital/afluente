from django.contrib import admin

from afluente.services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = 'service begin_date end_date'.split()
    ordering = ('service',)
