from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Program)
class ProgrameAdmin(admin.ModelAdmin):
    list_display = ("program_Created", "program_name")

admin.site.register(ProgramRegistration)