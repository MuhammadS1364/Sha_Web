from django.db import models
from django.contrib.auth.models import User

# Create your models here.

 
class Student_Model(models.Model):
    user_Stn = models.OneToOneField(User, on_delete=models.CASCADE)  # link with login user
    Student_Add_no = models.CharField(max_length=50, unique=True)
    Student_Name = models.CharField(max_length=250)
    Student_Phone = models.CharField(max_length=15)

    Student_Position = models.CharField(max_length=100)
    Student_Goal = models.CharField(max_length=250, null=True, blank=True)

    Student_Dob = models.DateField(default="2010-08-10")
    Student_Father = models.CharField(max_length=250)
    Student_Address = models.CharField(max_length=250)
    Student_Img = models.ImageField(upload_to='student_Box/')

    # Student OverAll Status
    
    Total_OutReachs = models.IntegerField(default=0, blank=True,null=True)
    Total_Class_Anjuman = models.IntegerField(default=0,blank=True,null=True)
    Tatal_Points = models.IntegerField(default=0, null=True,blank=True)


    def __str__(self):
        return f"{self.Student_Name}"


# Second for wing holder info model


class Wing_Model(models.Model):
    wing_user = models.OneToOneField(User, on_delete=models.CASCADE)  # link with login user
    Wing_Code = models.CharField(max_length=50, unique=True)
    Wing_Name = models.CharField(max_length=250, unique=True)

    Chair_Person = models.ForeignKey(
        Student_Model, on_delete=models.CASCADE,
        related_name="chairPerson_in_wings"
    )

    Assist_Person = models.ForeignKey(
        Student_Model, on_delete=models.CASCADE,
        related_name="assistant_in_wings"
    )
    wing_logo = models.ImageField(upload_to='wing_Box/')

    Total_Registered = models.IntegerField(default=0, blank=True,null=True)
    Total_ReSulted = models.IntegerField(default=0, blank=True,null=True)
    Total_Programed = models.IntegerField(default=0, null=True,blank=True)

    def __str__(self):
        return f"{self.Wing_Name}"
    


class Grallery_Model(models.Model):
    Grallery_Title = models.CharField(max_length=300)
    Grallery_Files = models.ImageField(upload_to="Gallery/", null=True,blank=True)
    Grallery_Vedio = models.FileField(upload_to="Vedio/", null=True,blank=True)

    def __str__(self):
        return f"{self.Grallery_Title}"
