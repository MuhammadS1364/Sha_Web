from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.decorators import login_required



# Import All the Forms and Models
from admin_panel.models import *
from .models import *
from .forms import *


# function for Creating A Outreach Model

def add_OutReach(request):
    if request.method == 'POST':

        # Geting the UserName who is Posting the Programes
        student_Obj = Student_Model.objects.get(user_Stn = request.user)

        # SubMitting the OutReach Form 
        new_Objt = OutReach_Form(request.POST, request.FILES)

        if new_Objt.is_valid():
            newOutReach_Obj = new_Objt.save(commit=False)
            newOutReach_Obj.student_name = student_Obj
            newOutReach_Obj.save()
            return redirect("Student_DashBoard")
        else:
            return HttpResponse("OutReach Programe Not add .......")
    else:
        new_Objt = OutReach_Form()

    return render(request, "addOutReach.html", {"form" : new_Objt})



# Returning all the OutReach for the Current User

def OutReach_List (request):

    # Getting the user Object , who is sending Request
    student = Student_Model.objects.get(user_Stn = request.user)

    # Sending all the List for the User 
    All_OutReach = OutReach_Model.objects.filter(student_name = student)

    return render (request, "outreach_list.html", {"OutReach" : All_OutReach})


