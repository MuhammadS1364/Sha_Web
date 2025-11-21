from django.db import models

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
    OutReach_date = models.DateField()
    OutReach_poster = models.ImageField(upload_to='OutReach/', blank=True,null=True)
    OutReach_discription = models.TextField(max_length=600)
    Total_OutReach = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.student_name} {self.OutReach_Programe_name} {self.OutReach_result}"



# Outreach Programes Model

class Achievements_Model(models.Model):
    Achiever = models.ForeignKey(
        Student_Model,
        on_delete=models.CASCADE
        )
    achieved_Title = models.CharField(max_length=250 )
    achiever_Result = models.CharField(max_length=250)
    achieveMent_Conductor = models.CharField(max_length=500)
    achieveMent_date = models.DateField()
    achieveMent_poster = models.ImageField(upload_to='AchieveMents/', blank=True,null=True)
    achieveMent_discription = models.TextField(max_length=600)
    Total_Achievements = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.Achiever} {self.achieved_Title} {self.achieveMent_poster}"
