from django import forms

from .models import *


# outReach Programes Form
class OutReach_Form (forms.ModelForm):
    class Meta:
        model = OutReach_Model
        fields = "__all__"

# Achievements Programes Form
class Achievements_Form (forms.ModelForm):
    class Meta:
        model = Achievements_Model
        fields = "__all__"
