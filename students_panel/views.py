from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



# Import All the Forms and Models
from admin_panel.models import *
from wing_panel.models import *
from students_panel.models import *
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

        outReach_Position = request.POST.get("OutReach_result")

        if not student_Obj:
            return HttpResponse("Error: You are not registered as a Student!")

        if student_Obj.Total_OutReachs is None:
            student_Obj.Total_OutReachs = 0
            student_Obj.save()
        
        if student_Obj.Tatal_Points is None:
            student_Obj.Tatal_Points = 0
            student_Obj.save()
        
        if student_Obj.Total_OutReachPoints is None:
            student_Obj.Total_OutReachPoints = 0
            student_Obj.save()
        
        # SubMitting the OutReach Form 
        new_Objt = OutReach_Form(request.POST, request.FILES)

        if new_Objt.is_valid():
            newOutReach_Obj = new_Objt.save(commit=False)

            newOutReach_Obj.student_name = student_Obj


            # Updating total OutReach in Student_Model
            student_Obj.Total_OutReachs += 1

            # Points Format for position 
            if outReach_Position == 'First':
                student_Obj.Total_OutReachPoints += 10
                student_Obj.Tatal_Points += 10
                newOutReach_Obj.Point_ForThis += 10
                student_Obj.save()

            elif outReach_Position == 'Second':
                student_Obj.Total_OutReachPoints += 7
                student_Obj.Tatal_Points += 7
                newOutReach_Obj.Point_ForThis += 7
                student_Obj.save()

            else:
                student_Obj.Total_OutReachPoints += 5
                student_Obj.Tatal_Points += 5
                newOutReach_Obj.Point_ForThis += 5
                student_Obj.save()

            newOutReach_Obj.save()
            
            student_Obj.save()
            print(f"Your total Outreach Point is: {student_Obj.Total_OutReachPoints} and total outReach Progrem is : {student_Obj.Total_OutReachs}")
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
        new_Objt = Ajnumame_Huda_Form(request.POST, request.FILES)

        # Checking if the Student is already registered this programe
        programe_name = request.POST.get("achieved_Title")
        if Ajnumame_Huda_Model.objects.filter(Achiever=student_Obj, achieved_Title=programe_name).exists():
            messages.error(request, "You have already registered for this Achievement Programe.")
            return redirect("Student_DashBoard")
        
        # For udating the Student and Achievements Model
        if student_Obj.Total_Anjuman_e_Huda is None:
            student_Obj.Total_Anjuman_e_Huda = 0
            student_Obj.save()

        # For udating the Student and Achievements Model
        if student_Obj.Total_AnjumanHudaPoints is None:
            student_Obj.Total_AnjumanHudaPoints = 0
            student_Obj.save()

        # For updating the Student and Achievements points
        if student_Obj.Tatal_Points is None:
            student_Obj.Tatal_Points = 0
            student_Obj.save()
        

        if new_Objt.is_valid():
            newAchieve_Obj = new_Objt.save(commit=False)

            newAchieve_Obj.Achiever = student_Obj

            # Updating total Achievements in Student_Model
            student_Obj.Total_Anjuman_e_Huda += 1

            # Points Format for position
            if newAchieve_Obj.achiever_Result == 'First':
                points = 10
            elif newAchieve_Obj.achiever_Result == 'Second':
                points = 7
            else:
                points = 4
            
                
            newAchieve_Obj.Point_ForThis += points
            student_Obj.Tatal_Points += points
            student_Obj.Total_AnjumanHudaPoints += points


            newAchieve_Obj.save()
            student_Obj.save()


            return redirect("Student_DashBoard")
        else:
            return HttpResponse("Achievement Programe Not add, Validation Error .......")

            
    else:
        new_Objt = Ajnumame_Huda_Form()

    return render(request, "addAchieve.html", {"form" : new_Objt})



# Returning all the OutReach for the Current User

def OutReach_List (request):

    All_OutReach = OutReach_Model.objects.all()

    return render (request, "outreach_list.html", {"OutReach" : All_OutReach})


# Edite OutReach programe

def EditeOutReach(request, programe_id):
   
    to_Edite = OutReach_Model.objects.get(id = programe_id)
    act_student = Student_Model.objects.get(user_Stn = request.user)

    # Before Point for this Object 
    Pre_Point = to_Edite.Point_ForThis

    if request.method == 'POST':


        # form for editing Outreach Programe

        form = Edite_OutReach(request.POST, request.FILES,instance=to_Edite)
        OutReach_result = request.POST.get("OutReach_result")

        if form.is_valid():
            edited_OutReach = form.save(commit=False)

            # Position Changing, Points changes
            print(f"the ponti was is : {Pre_Point}")
            to_Edite.Point_ForThis -= Pre_Point
            act_student.Tatal_Points -= Pre_Point 
            act_student.Total_OutReachPoints -= Pre_Point

            # if he have change in Position 
            if OutReach_result == 'First':
                act_student.Total_OutReachPoints += 10
                act_student.Tatal_Points += 10
                to_Edite.Point_ForThis += 10
                act_student.save()

            elif OutReach_result == 'Second':
                act_student.Total_OutReachPoints += 7
                act_student.Tatal_Points += 7
                to_Edite.Point_ForThis += 7
                act_student.save()

            elif OutReach_result == 'Third':
                act_student.Total_OutReachPoints += 5
                act_student.Tatal_Points += 5
                to_Edite.Point_ForThis += 5
                act_student.save()

            else:
                act_student.Total_OutReachPoints = Pre_Point
                act_student.Tatal_Points = Pre_Point
                to_Edite.Point_ForThis = Pre_Point 
                act_student.save()

            edited_OutReach.save()
            print(f"After edited {edited_OutReach.Point_ForThis}")
            return redirect("Student_DashBoard")

    else:
        form = Edite_OutReach(instance=to_Edite)
    
    return render(request, 'editeOutReach.html', {
        "form" : form,
        "all_OutReact" : to_Edite
    })
    



    # to delect OutReach 

def DeleteOutReach(request, programe_id):
    toDel_Programe = OutReach_Model.objects.get(id=programe_id)
    theStudent = Student_Model.objects.get(user_Stn = request.user)

    Point_Programe = toDel_Programe.Point_ForThis

    # subtract the uploaded markin model 
    theStudent.Total_OutReachPoints -= Point_Programe
    theStudent.Tatal_Points -= Point_Programe
    theStudent.Total_OutReachs -= 1 
    theStudent.save()

    toDel_Programe.delete()
    

    messages.success(request, "Your OutReach Info Deleted........")
    return redirect("Student_DashBoard")

        


def EditeAchievements(request,programe_id):
    form = Ajnumame_Huda_Form()
    return render(request, "addAchieve.html", {"form":form})





def DeleteAchievements(request, programe_id):
    toDel_Achieve = Ajnumame_Huda_Model.objects.get(id = programe_id)
    theStudent = Student_Model.objects.get(user_Stn = request.user)

    Point_Programe = toDel_Achieve.Point_ForThis

    print(f"achievement point is: {Point_Programe}")
    # subtract the uploaded markin model 
    theStudent.Total_AnjumanHudaPoints -= Point_Programe
    theStudent.Tatal_Points -= Point_Programe
    theStudent.Total_Anjuman_e_Huda -= 1 


    theStudent.save()
    toDel_Achieve.delete()
    

    messages.success(request, "Your Achievement Info Deleted........")
    return redirect("Student_DashBoard")

        

        