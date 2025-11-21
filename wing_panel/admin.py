from django.contrib import admin

# Register your models here.

from .models import *

class Programe_Admin(admin.ModelAdmin):
    list_display = ["Program_Created", "Program_name"]

admin.site.register(Program_Bank, Programe_Admin)

class Candidates_Registration_Admin(admin.ModelAdmin):
    list_display = ["wing_name", "Registered_Programe"]

admin.site.register(Candidates_Registration_Model,Candidates_Registration_Admin)
