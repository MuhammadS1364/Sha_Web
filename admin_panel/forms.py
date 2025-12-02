from django import forms
from .models import *
from django.core.exceptions import ValidationError
import datetime
from django.utils.translation import gettext_lazy as _
from django.utils import timezone 




class Student_form(forms.ModelForm):
    class Meta :
        model = Student_Model
        fields = "__all__"
        exclude = ["is_Controller","user_Stn","Total_OutReachs","Total_Anjuman_e_Huda","Total_Self_Creations","Total_ClassProgrames","Total_Registered","Total_ReSulted","Tatal_Points","Total_OutReachPoints","Total_SelfCreationPoints","Total_ClassProgramesPoints","Total_AnjumanHudaPoints"]
        widgets = {
            "Student_Dob" : forms.DateInput(attrs={
                "type" : "date"
            }),
            "Student_Img" : forms.ClearableFileInput(attrs={
                "type" : "file"
            }),
        }

        

# 
class Wing_form(forms.ModelForm):
    class Meta :
        model = Wing_Model
        fields = "__all__"
        exclude = ["wing_user","Chair_Person","Assist_Person","Total_Registered","Total_ReSulted",""]
        widgets = {
            "wing_logo" : forms.ClearableFileInput(attrs={
                "type" : "file"
            }),
        }

        

class Grallery_form(forms.ModelForm):
    class Meta :
        model = Gallery_Model
        fields = "__all__"

        widgets = {
            "Grallery_Files" : forms.ClearableFileInput(attrs={
                "type" : "file"
            }),
            "Grallery_Vedio" : forms.ClearableFileInput(attrs={
                "type" : "file"
            }),
        }

        # Some custom validation can be added here if needed
        def clean_Grallery_Files(self):
            file = self.cleaned_data.get('Grallery_Files')

            if file and not file.name.endswith(('.jpg', '.jpeg', '.png')):
                raise forms.ValidationError("Invalid file format. Please upload an image file.")
            
            return file
        
        def clean_Grallery_Vedio(self):
            vedio = self.cleaned_data.get('Grallery_Vedio')

            if vedio and not vedio.name.endswith(('.mp4', '.avi', '.mov')):
                raise forms.ValidationError("Invalid file format. Please upload a video file.")
            
            return vedio
