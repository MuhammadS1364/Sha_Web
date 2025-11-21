from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages


from .forms import *
from students_panel.models import *
from wing_panel.models import *


def login_view (request):
    if request.method == 'POST':
        userName = request.POST.get("username")
        userPass = request.POST.get("password")

              # Step 1: Check if entered value is email
        # if User.objects.filter(email=userName).exists():
        #     user_obj = User.objects.get(email=userName)
        #     # print(user_obj.email, "it is .....")
        #     final_username = user_obj.email
        # else:
        #     messages.error(request,f"Login Failed. {request.user}, May be your email")
        #     final_username = userName
        #     return render(request, "login_user.html")

        act_user = authenticate(request, username = userName , password = userPass)

        if act_user is not None:

            login(request, act_user)

            # log in Redirect 
            if act_user.is_superuser:
                return redirect("Admin_DashBoard")
            elif act_user.is_staff:
                return redirect("Wing_DashBoard")
            else:
                return redirect("Student_DashBoard")

        else:
            messages.error(request,f"Login Failed. {request.user}, technical issu")
            return render(request, "login_user.html")


    return render(request, "login_user.html")



def logout_view(request):
    logout(request)
    return redirect("login_view")


# Creating New User for Administration 

def newUser (request):

    if request.method == 'POST':

    #    form = User(request.POST, request.FILES)
       userName = request.POST.get('userName')
       userEmail = request.POST.get('userEmail')
       userPass1 = request.POST.get('userPass1')
       userPass2 = request.POST.get('userPass2')
       userRole = request.POST.get('userRole')


    #    Protecting the Dobble User Error 
       if User.objects.filter(username = userName).exists():
           messages.error(request , "This User Already Exist.....")
           return redirect("login_view")

       
       if userPass1 == userPass2:
            new_user = User.objects.create_user(
                username= userName,
                email = userEmail,
                password = userPass1,
            )

            # Assigning User Role 

            if userRole == "Admin":
                new_user.is_superuser = True
                new_user.is_staff = True
                new_user.save()
                
                login(request, new_user)
                
                return redirect("Admin_DashBoard")
                
            elif userRole == "Wing":
                new_user.is_superuser = False
                new_user.is_staff = True
                new_user.save()

                return redirect("add_wing")

            else:
                new_user.is_superuser = False
                new_user.is_staff = False
                new_user.save()

                return redirect("add_student")
            
       else:
           messages.error(request ,"Password1 did Not Match to Password2!, Plz Check It...")
           form = User()
           return render(request, "addUser.html", {"form":form})

            
           
    else:
        form = User()
        
    return render(request, "addUser.html", {"form":form})


def add_student(request):
    # Sending All User objects
    all_User = User.objects.all()

    if request.method == 'POST':

        newStdn_Form = Student_form(request.POST, request.FILES)

        new_stn_user = request.POST.get("user_Stn")

        new_stn_addNo = request.POST.get("Student_Add_no")


        if Student_Model.objects.filter(Student_Add_no=new_stn_addNo).exists():
            messages.error(request, "Student Already Exists")
            return redirect("login_view")
                
        if newStdn_Form.is_valid():

            newStn_Obj = User.objects.get(id=new_stn_user)


            new_Student = newStdn_Form.save(commit=False)
            new_Student.user_Stn = newStn_Obj
            new_Student.save()

            messages.success(request, "Student Added Successfully")
            login(request, newStn_Obj)
            return redirect("Student_DashBoard")
        else:
            messages.error(request, "This Form is not Valid Form , plz check.")
            return render(request, 'addStudent.html', {
        "form": newStdn_Form,
        "all_User" : all_User
        })

    else:
        newStdn_Form = Student_form()

    return render(request, 'addStudent.html', {
        "form": newStdn_Form,
        "all_User" : all_User
        })



# Add New Wing

def add_wing(request):
    all_Users = User.objects.all()
    if request.method == 'POST':

        newWing_Form = Wing_form(request.POST,request.FILES )

        wing_user = request.POST.get("wing_user")

        if newWing_Form.is_valid():

            # Getting the New User Object
            newWing_Obj = User.objects.get(id=wing_user)

            print(f"Wing User is : {newWing_Obj}")


            new_Wing = newWing_Form.save(commit=False)
            new_Wing.wing_user = newWing_Obj
            new_Wing.save()

            login(request, newWing_Obj)
            # Return their data to the DashBoard 
            return redirect("Wing_DashBoard")
        else:
            messages.error(request ,"Validation Problem.........")
            return render(request, 'addWing.html', {
        "form": newWing_Form,
        "all_Users" :all_Users
        })
    else:
        newWing_Form = Wing_form()
        
    return render(request, 'addWing.html', {
        "form": newWing_Form,
        "all_Users" :all_Users
        })



# Admin Dash Board

def Admin_DashBoard(request):

    # Rendering All The Data to Admin DashBoard

    all_Users = User.objects.all()
    all_students = Student_Model.objects.all()
    all_Wings = Wing_Model.objects.all()

    context = {
       "all_Users" :  all_Users,
       "all_students" :  all_students,
       "all_Wings" :  all_Wings,
    }
    return render(request, "admin_dashboard.html", context)

# Wing Dash Board

def Wing_DashBoard(request):
    act_wing = Wing_Model.objects.get(wing_user = request.user)
    all_Programe = Program_Bank.objects.filter(Program_Created = act_wing)
    context = {
        "act_wing" : act_wing,
        "all_Programe" : all_Programe
    }
    return render(request, "wing_dashboard.html", context)


# Student DashBoard

def Student_DashBoard(request):
    act_stn = User.objects.get(user_Stn = request.user)

    All_OutReach = OutReach_Model.objects.filter(student_name = act_stn)
    All_Achievements = Achievements_Model.objects.filter(Achiever = act_stn)

    context = {
        "act_stn" : act_stn,
        "All_OutReach" : All_OutReach,
        "All_Achievements" : All_Achievements
    }
    return render(request, "student_dashboard.html", context)




# edite functions 

def editePassword(request):
    if request.method == 'POST':
        userName = request.POST.get("userName")
        userPass1 = request.POST.get("userPass1")
        userPass2 = request.POST.get("userPass2")


        # get the User Object 
        if userName:

            if userPass1 != userPass2:
                return messages.error("Password 2 doesnto Matched.........")

            toChange = User.objects.get(username = userName)

            toChange.set_password(userPass1)
            toChange.save()

            return redirect("login_view")
        else:
            return messages.error("Username not received from form!")


    return render(request, "forgot.html")


# error pages 
