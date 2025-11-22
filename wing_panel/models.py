from django.db import models
from django.utils import timezone
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
   Program_date = models.DateField(default=timezone.now)
   Program_poster = models.ImageField(upload_to="Programs/", blank=True, null=True)

    # Program Status
   is_Registration_Active = models.BooleanField(default=True, blank=True, null=True)
   is_Resulted = models.BooleanField(default=False, blank=True, null=True)            
   Total_Programes = models.IntegerField(default=0, blank=True, null=True)        


   def __str__(self):
       return f"{self.Program_name} {self.Program_Created}"

class Candidates_Registration_Model(models.Model):
    Candidates_Name = models.ForeignKey(Student_Model,on_delete = models.CASCADE)  
    Registered_Programe = models.ForeignKey(Program_Bank, on_delete=models.CASCADE)

    def __str__(self):
        return f"Registrations for {self.Registered_Programe}"

# Result upload Model

class Upload_Result(models.Model):
    
    Result_Uploaded_By = models.ForeignKey(Wing_Model, on_delete=models.CASCADE)

    Result_Programe = models.ForeignKey(Program_Bank, on_delete=models.CASCADE)

    Position_Holder1 = models.ForeignKey(
        Student_Model,
        on_delete=models.CASCADE,
        related_name='position_holder_1',
        blank=True,
        null=True
        )
    Position_Holder1_img = models.ImageField(upload_to="Resulted_img/", blank=True, null=True)

    Position_Holder2 = models.ForeignKey(
        Student_Model,
        on_delete=models.CASCADE,
        related_name='position_holder_2',
        blank=True,
        null=True
        )
    Position_Holder2_img = models.ImageField(upload_to="Resulted_img/", blank=True, null=True)


    Position_Holder3 = models.ForeignKey(
        Student_Model,
        on_delete=models.CASCADE,
        related_name='position_holder_3',
        blank=True,
        null=True
        )

    Position_Holder3_img = models.ImageField(upload_to="Resulted_img/", blank=True, null=True)

    Result_Baner = models.FileField(upload_to="Results/", blank=True, null=True)

    def __str__(self):
        return f"Result for {self.Result_Programe} First is {self.Position_Holder1}"