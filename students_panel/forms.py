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

        def clean_OutReach_date(self):
            date = self.cleaned_data.get("OutReach_date")
            if date > timezone.now().date():
                raise ValidationError(_("The date cannot be in the future."))
            return date

        def clean_OutReach_poster(self):
            poster = self.cleaned_data.get("OutReach_poster")
            if poster:
                if poster.endswith('.jpg') or poster.endswith('.png') or poster.endswith('.jpeg'):
                    raise ValidationError(_("Invalid file extention Only jpg, png ,jpeg allowed ."))
            return poster

# Achievements Programes Form
class Achievements_Form (forms.ModelForm):
    class Meta:
        model = Achievements_Model
        # fields = "__all__"
        exclude = ["Achiever"]
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