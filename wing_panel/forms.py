from django import forms

from .models import *

class Add_Program_Form(forms.ModelForm):
    class Meta:
        model = Program_Bank
        exclude = ["Program_Created","Tatal_Registrations", "is_Registration","is_Resulted"]
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
        model = Result_Bank_Model
        fields = '__all__'
        exclude = ['Result_Uploaded_By', 'Result_Programe', 'Position_Holder1','Position_Holder1_Mark','Position_Holder2','Position_Holder2_Mark','Position_Holder3','Position_Holder3_Mark','Grande_Holder','Grande_Holder_Mark']
