from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



# Import All the Forms and Models
from admin_panel.models import *
from .models import *
from .forms import *


# function for Creating A Outreach Model
@login_required
def add_OutReach(request):

    # Preventing for other User except of Students
    if request.user.is_superuser or  request.user.is_staff:
        messages.error(request, "You are a Student User, It is Only for Students's Users... ")
        logout(request)
        return redirect("login_view")
    
    


    if request.method == 'POST':

        # Geting the UserName(Linked-in ot User) who is Posting the Programes
        student_Obj = Student_Model.objects.filter(user_Stn=request.user).first()

        if not student_Obj:
            return HttpResponse("Error: You are not registered as a Student!")

        if student_Obj.Total_OutReachs is None:
            student_Obj.Total_OutReachs = 0
            student_Obj.save()
        
        # SubMitting the OutReach Form 
        new_Objt = OutReach_Form(request.POST, request.FILES)

        if new_Objt.is_valid():
            newOutReach_Obj = new_Objt.save(commit=False)

            newOutReach_Obj.student_name = student_Obj
            newOutReach_Obj.save()

            # Updating total OutReach in Student_Model
            student_Obj.Total_OutReachs += 1
            student_Obj.save()
            return redirect("Student_DashBoard")
        else:
            return HttpResponse("OutReach Programe Not add, Validation Error .......")
    else:
        new_Objt = OutReach_Form()

    return render(request, "addOutReach.html", {"form" : new_Objt})



# function for Creating A Outreach Model
@login_required
def add_AchieveMents(request):
    
    # Preventing for other User except of Students
    if request.user.is_superuser or  request.user.is_staff:
        messages.error(request, "You are a Student User, It is Only for Students's Users... ")
        logout(request)
        return redirect("login_view")


    if request.method == 'POST':

        user_Objt = User.objects.get(username = request.user)
        # Geting the UserName(Linked-in ot User) who is Posting the Programes
        student_Obj = Student_Model.objects.get(user_Stn = user_Objt)

        # SubMitting the OutReach Form 
        new_Objt = Achievements_Form(request.POST, request.FILES)

        if new_Objt.is_valid():
            newAchieve_Obj = new_Objt.save(commit=False)

            newAchieve_Obj.Achiever = student_Obj
            newAchieve_Obj.save()

            return redirect("Student_DashBoard")
        else:
            return HttpResponse("Achievement Programe Not add, Validation Error .......")
    else:
        new_Objt = Achievements_Form()

    return render(request, "addAchieve.html", {"form" : new_Objt})



# Returning all the OutReach for the Current User

def OutReach_List (request):

    All_OutReach = OutReach_Model.objects.all()

    return render (request, "outreach_list.html", {"OutReach" : All_OutReach})


