from django import forms
from .models import *



class Student_form(forms.ModelForm):
    class Meta :
        model = Student_Model
        fields = "__all__"


class Wing_form(forms.ModelForm):
    class Meta :
        model = Wing_Model
        fields = "__all__"