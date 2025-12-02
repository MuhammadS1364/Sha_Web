from django.contrib import admin

# Register your models here.

from .models import *

class Programe_Admin(admin.ModelAdmin):
    list_display = ["Program_Created", "Program_name", "Tatal_Registrations","is_Registration", "is_Resulted"]

admin.site.register(Program_Bank, Programe_Admin)

class Candidates_Registration_Admin(admin.ModelAdmin):
    list_display = ["Candidates_Name","Registered_Programe"]

admin.site.register(Candidates_Registration_Model,Candidates_Registration_Admin)

class Result_Bank_Admin(admin.ModelAdmin):
    list_display = ["Result_Uploaded_By","Result_Programe","Position_Holder1","Position_Holder2"]
admin.site.register(Result_Bank_Model,Result_Bank_Admin)