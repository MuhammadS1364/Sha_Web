from django.db import models

# Create your models here.

# from .forms import *
from admin_panel.models import *
from students_panel.models import *
from wing_panel.models import *


# Wing programe registration Model
class Program(models.Model):
    program_Created = models.ForeignKey(Wing_Model, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=200)
    program_date = models.DateField()
    program_poster = models.ImageField(upload_to="Programs/", blank=True, null=True)
    program_disc = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.program_name} {self.program_Created}"



class ProgramRegistration(models.Model):
    wing_name = models.ForeignKey(Wing_Model, on_delete=models.CASCADE,)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student_Model)   # MANY STUDENTS

    def __str__(self):
        return f"Registrations for {self.program.program_name}"

# Result upload Model