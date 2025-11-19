from django import forms

from .models import *


# outReach Programes Form
class OutReach_Form (forms.ModelForm):
    class Meta:
        model = OutReach_Model
        fields = "__all__"
        exclude = ["student_name"]

# Achievements Programes Form
class Achievements_Form (forms.ModelForm):
    class Meta:
        model = Achievements_Model
        fields = "__all__"
        exclude = ["Achiever"]
        widgets = {
             "programe_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),
             "programe_poster": forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }