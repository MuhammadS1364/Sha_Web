from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# first for Studnet basic Info Model

class Student_info_Model(models.Model):
    user_Stn = models.OneToOneField(User, on_delete=models.CASCADE)  # link with login user
    Student_Add_no = models.CharField(max_length=50, unique=True)
    Student_Name = models.CharField(max_length=250, unique=True)
    Student_Email = models.EmailField(unique=True, primary_key=True)
    Student_Phone = models.CharField(max_length=15)
    Student_Father = models.CharField(max_length=250)
    Student_Address = models.CharField(max_length=250)
    Student_Img = models.ImageField(upload_to='student/')

class Wing_Model(models.Model):
    wing_user = models.OneToOneField(User, on_delete=models.CASCADE)  # link with login user
    Wing_Code = models.CharField(max_length=50, unique=True)
    Wing_Name = models.CharField(max_length=250, unique=True)
    Wing_Email = models.EmailField(unique=True, primary_key=True)
    Chair_Person = models.CharField(max_length=15)
    Assist_Person = models.CharField(max_length=15)

 
# class Student_info_Model(models.Model):
#     user_Stn = models.OneToOneField(User, on_delete=models.CASCADE)  # link with login user
#     Student_Add_no = models.CharField(max_length=50, unique=True)
#     Student_Name = models.CharField(max_length=250, unique=True)
#     Student_Email = models.EmailField(unique=True, primary_key=True)
#     Student_Phone = models.CharField(max_length=15)

#     Student_Position = models.CharField(max_length=100)
#     Student_Goal = models.CharField(max_length=250, null=True, blank=True)

#     Student_Dob = models.DateField(default="2010-08-10")
#     Student_Father = models.CharField(max_length=250)
#     Student_Address = models.CharField(max_length=250)
#     Student_Img = models.ImageField(upload_to='student/')

#     def __str__(self):
#         return f"{self.Student_Add_no} - {self.Student_Name}"



# Second for wing holder info model
