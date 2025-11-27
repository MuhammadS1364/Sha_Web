from django.contrib import admin

# Register your models here.
from .models import *

class Student_Admin_Model(admin.ModelAdmin):
    list_display = ["user_Stn","Student_Add_no","Student_Name","Student_Goal","Student_Father",]

admin.site.register(Student_Model, Student_Admin_Model)


class Wing_Admin_Model(admin.ModelAdmin):
    list_display = ["wing_user","Wing_Code","Wing_Name","Chair_Person","Assist_Person"]
    
admin.site.register(Wing_Model, Wing_Admin_Model)
