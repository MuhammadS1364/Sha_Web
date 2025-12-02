from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
from admin_panel.models import *


# Outreach Programes Model

class OutReach_Model(models.Model):
    student_name = models.ForeignKey(
        Student_Model,
        on_delete=models.CASCADE
        )
    OutReach_Programe_name = models.CharField(max_length=250 )
    OutReach_result = models.CharField(max_length=250)
    OutReach_Conductor = models.CharField(max_length=500)
    OutReach_date = models.DateField(default=timezone.now)
    OutReach_poster = models.ImageField(upload_to='OutReach/', blank=True,null=True)
    OutReach_discription = models.TextField(max_length=600)

    def __str__(self):
        return f"{self.student_name} {self.OutReach_Programe_name} {self.OutReach_result}"



# Outreach Programes Model

class Ajnumame_Huda_Model(models.Model):
    Achiever = models.ForeignKey(
        Student_Model,
        on_delete=models.CASCADE
        )
    achieved_Title = models.CharField(max_length=250 )
    achiever_Result = models.CharField(max_length=250)
    achieveMent_Conductor = models.CharField(max_length=500)
    achieveMent_date = models.DateField(default=timezone.now)
    achieveMent_poster = models.ImageField(upload_to='AchieveMents/', blank=True,null=True)
    achieveMent_discription = models.TextField(max_length=600)

    # Total Achiever Status 
    Total_Achievements = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.Achiever} {self.achieved_Title} {self.achiever_Result}"


# Self Creation Program Bank Model
class Self_Creations_Bank(models.Model):
    creator_Student = models.ForeignKey(
        Student_Model,
        on_delete=models.CASCADE
        )
    Creation_Title = models.CharField(max_length=250)
    Creation_Description = models.TextField(max_length=1000)
    Creation_Date = models.DateField(default = timezone.now)
    Creation_File = models.FileField(upload_to='Self_Creations/', blank=True,null=True)

    def __str__(self):
        return f"{self.creator_Student} {self.Creation_Title}"