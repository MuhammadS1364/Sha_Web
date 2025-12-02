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
    is_Controller = models.BooleanField(null=True, blank=True, default=False)
    
    # Student OverAll Status
    Total_OutReachs = models.IntegerField(default=0)
    Total_Anjuman_e_Huda = models.IntegerField(default=0)
    Total_Self_Creations = models.IntegerField(default=0)
    Total_ClassProgrames = models.IntegerField(default=0)

    # TOTAL Registrations and Resulted 
    Total_Registered = models.IntegerField(default=0)
    Total_ReSulted = models.IntegerField(default=0)
    # POINTS TABLE
    Tatal_Points = models.IntegerField(default=0)
    Total_OutReachPoints = models.IntegerField(default=0)
    Total_SelfCreationPoints = models.IntegerField(default=0)
    Total_ClassProgramesPoints = models.IntegerField(default=0)
    Total_AnjumanHudaPoints = models.IntegerField(default=0)

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

    Total_Registered = models.IntegerField(default=0)
    Total_ReSulted = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.Wing_Name}"
    


class Gallery_Model(models.Model):
    Created_by = models.ForeignKey(
        Wing_Model,
        on_delete=models.CASCADE, default=None
        )
    Gallery_Title = models.CharField(max_length=300)
    Gallery_Files = models.ImageField(upload_to="Gallery/", null=True,blank=True)
    Gallery_Vedio = models.FileField(upload_to="Vedio/", null=True,blank=True)
    Gallery_Dic = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.Gallery_Title}"
