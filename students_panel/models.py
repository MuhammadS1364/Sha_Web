from django.db import models

# Create your models here.
from admin_panel.models import *


# Outreach Programes Model

class OutReach_Model(models.Model):
    student_name = models.ForeignKey(
        Student_Model,
        on_delete=models.CASCADE
        )
    programe_name = models.CharField(max_length=250 )
    result = models.CharField(max_length=250)
    programe_Conductor = models.CharField(max_length=500)
    programe_date = models.DateField()
    programe_poster = models.ImageField(upload_to='OutReach/', blank=True,null=True)
    programe_discription = models.TextField(max_length=600)
    
    def __str__(self):
        return f"{self.student_name} {self.programe_name} {self.result}"



# Outreach Programes Model

class Achievements_Model(models.Model):
    Achiever = models.ForeignKey(
        Student_Model,
        on_delete=models.CASCADE
        )
    achieved_Title = models.CharField(max_length=250 )
    resulted = models.CharField(max_length=250)
    achieveMent_Conductor = models.CharField(max_length=500)
    achieveMent_date = models.DateField()
    achieveMent_poster = models.ImageField(upload_to='AchieveMents/', blank=True,null=True)
    achieveMent_discription = models.TextField(max_length=600)

    
    def __str__(self):
        return f"{self.Achiever} {self.achieved_Title} {self.resulted}"
