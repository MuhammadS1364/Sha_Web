from django import forms

from .models import *

class Add_Program_Form(forms.ModelForm):
    class Meta:
        model = Program_Bank
        exclude = ["Program_Created"]
        widgets = {
            "Program_date": forms.DateInput(attrs={'type': 'date'}),
            "Program_poster": forms.ClearableFileInput(attrs={'class': 'form-control'}),               
            
        }

        
class Candidate_Registration_Form(forms.ModelForm):
    class Meta:
        model = Candidates_Registration_Model
        exclude = ["Candidates_Name", "Registered_Programe"]


class Upload_Result_Form(forms.ModelForm):
    class Meta:
        model = Upload_Result
        # exclude = ["Result_Uploaded_By", "Result_Programe"]
        fields = ["Position_Holder1_img", "Position_Holder2_img", "Position_Holder3_img", "Result_Baner", "Grande_Holder"]
        widgets = {
            "Result_Baner": forms.ClearableFileInput(attrs={'class': 'form-control'}),
            "Position_Holder1_img": forms.ClearableFileInput(attrs={'class': 'form-control'}),
            "Position_Holder2_img": forms.ClearableFileInput(attrs={'class': 'form-control'}),
            "Position_Holder3_img": forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }