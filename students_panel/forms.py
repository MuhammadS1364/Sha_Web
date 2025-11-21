from django import forms

from .models import *


# outReach Programes Form
class OutReach_Form (forms.ModelForm):
    class Meta:
        model = OutReach_Model
        fields = "__all__"
        exclude = ["student_name"]
        widgets = {
            "OutReach_date" : forms.DateInput(attrs={
                "type" : "date"
            })
        }

# Achievements Programes Form
class Achievements_Form (forms.ModelForm):
    class Meta:
        model = Achievements_Model
        fields = "__all__"
        exclude = ["Achiever"]
        widgets = {
             "achieveMent_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),
             "achieveMent_poster": forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }