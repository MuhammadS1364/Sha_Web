from django import forms

from .models import *

class Add_Program_Form(forms.ModelForm):
    class Meta:
        model = Program
        exclude = ["program_Created"]
        widgets = {
            "program_date": forms.DateInput(attrs={'type': 'date'}),
        }
class Registration_Programe(forms.ModelForm):
    class Meta:
        model = ProgramRegistration
        exclude = ["wing_name","program"]
        # widgets = {
        #     "program_date": forms.DateInput(attrs={'type': 'date'}),
        # }
