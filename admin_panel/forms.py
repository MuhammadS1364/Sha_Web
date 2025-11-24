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
        widgets = {
            "Student_Dob" : forms.DateInput(attrs={
                "type" : "date"
            }),
            "Student_Img" : forms.ClearableFileInput(attrs={
                "type" : "file"
            }),
        }

        # Some custom validation can be added here if needed
        def clean_Student_Phone(self):
            phone = self.cleaned_data.get('Student_Phone')

            if len(phone) < 10:
                raise forms.ValidationError("Phone number must be at least 10 digits long.")
            
            return phone
        
        def clean_Student_DOB(self):
            dob = self.cleaned_data.get('Student_Dob')
            # Additional DOB validation logic can be added here
            if dob >= datetime.date.today():
                raise forms.ValidationError("Date of Birth must be in the past.")
            
            if dob < datetime.date(2010, 1, 1):
                raise forms.ValidationError("Date of Birth is too far in the past.")
            return dob
        
        

# 
class Wing_form(forms.ModelForm):
    class Meta :
        model = Wing_Model
        fields = "__all__"

        widgets = {
            "wing_logo" : forms.ClearableFileInput(attrs={
                "type" : "file"
            }),
        }

        # Some custom validation can be added here if needed
        def clean_Wing_Code(self):
            code = self.cleaned_data.get('Wing_Code')

            if len(code) < 4:
                raise forms.ValidationError("Wing Code must be at least 4 characters long.")

            return code
        
        def clean_Wing_Logo(self):
            logo = self.cleaned.data.get('wing_logo')

            if logo.endswith(('.jpg', '.jpeg', '.png')):
                return logo
            else:
                raise forms.ValidationError("Invalid file format. Please upload an image file.")



class Grallery_form(forms.ModelForm):
    class Meta :
        model = Grallery_Model
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
