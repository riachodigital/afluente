from django.contrib import admin

from afluente.customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ('name',)
