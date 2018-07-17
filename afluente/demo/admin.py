from django.contrib import admin

# Register your models here.
from afluente.demo.models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = 'nome status servico'.split()
    ordering = ('nome',)
