from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone 

import datetime
from .models import *

# outReach Programes Form
class OutReach_Form (forms.ModelForm):
    class Meta:
        model = OutReach_Model
        # fields = "__all__"
        exclude = ["student_name"]
        widgets = {
            "OutReach_date" : forms.DateInput(attrs={
                "type" : "date"
            }),
            "OutReach_poster": forms.ClearableFileInput(attrs={
                'class': 'file-input',
            }),
            "OutReach_discription": forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
        }


# Achievements Programes Form
class Ajnumame_Huda_Form (forms.ModelForm):
    class Meta:
        model = Ajnumame_Huda_Model
        # fields = "__all__"
        exclude = ["Achiever","Total_Achievements"]
        widgets = {
             "achieveMent_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),
             "achieveMent_poster": forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            "achieveMent_discription": forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
        }