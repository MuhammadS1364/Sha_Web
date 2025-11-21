from django.db import models

# Create your models here.

# from .forms import *
from admin_panel.models import *
from students_panel.models import *
from wing_panel.models import *


# Wing programe registration Model
class Program_Bank(models.Model):
   Program_Created = models.ForeignKey(Wing_Model, on_delete=models.CASCADE)
   Program_name = models.CharField(max_length=200)
   Program_Venue = models.CharField(max_length=250)
   Program_date = models.DateField(auto_now=True)
   Program_poster = models.ImageField(upload_to="Programs/", blank=True, null=True)

   def __str__(self):
       return f"{self.Program_name} {self.Program_Created}"

class Candidates_Registration_Model(models.Model):
    wing_name = models.ForeignKey(Wing_Model, on_delete=models.CASCADE,)
    Registered_Programe = models.ForeignKey(Program_Bank, on_delete=models.CASCADE)
    Candidates_Name = models.CharField(max_length=230)  

    def __str__(self):
        return f"Registrations for {self.Registered_Programe}"

# Result upload Model