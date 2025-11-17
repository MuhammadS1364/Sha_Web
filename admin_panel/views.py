from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout





from .forms import *


def login_view (request):
    if request.method == 'POST':
        userName = request.POST.get("username")
        userPass = request.POST.get("password")
        act_user = authenticate(request, username = userName, password = userPass)
        if act_user is not None:
            login(request, act_user)
            return HttpResponse(f"Hello, {request.user}!")
        else:
            return HttpResponse(f"Hello, {request.user}!, login failed......")

    return render(request, "login_user.html")

def logout_view(request):
    logout(request)
    return redirect("logout_view")




# Creating New User for Administration 

def newUser (request):
    if request.method == 'POST':

    #    form = User(request.POST, request.FILES)

       userName = request.POST.get('userName')
       userEmail = request.POST.get('userEmail')
       userPass1 = request.POST.get('userPass1')
       userPass2 = request.POST.get('userPass2')
       userRole = request.POST.get('userRole')
       print(userRole)
    #    Protecting the Dobble User Error 
       if User.objects.filter(username = userName).exists():
           return HttpResponse("This User Already Exist.....")

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

                # redirect to the Admin DashBoard
                return redirect("Admin_DashBoard")
                
            elif userRole == "Wing":
                new_user.is_superuser = False
                new_user.is_staff = True
                new_user.save()

                # redirect to the Wing DashBoard
                return redirect("Wing_DashBoard")

            else:
                new_user.is_superuser = False
                new_user.is_staff = False
                new_user.save()

                # redirect to the Student DashBoard
                return redirect("Student_DashBoard")
       else:
           return HttpResponse("Password 2 is not match.....")
            
            # HttpResponse("No!, New User Not Created...")
    else:
        form = User()
        
    return render(request, "addUser.html", {"form":form})


# def add_student(request):
#     if request.method == 'POST':

#         new_stn_form = Student_form(request.POST,request.FILES )

#         if new_stn_form.is_valid():
#             new_stn_form.save()
#             return HttpResponse("Student Added.........")
#         else:
#             return HttpResponse("Student Not Added.........")
#     else:
#         new_stn_form = Student_form()
#     return render(request, 'addUser.html', {"form": new_stn_form})


# Admin Dash Board

def Admin_DashBoard(request):
    return render(request, "admin_dashboard.html")

# Wing Dash Board

def Wing_DashBoard(request):
    return render(request, "student_dashboard.html")


# Student DashBoard

def Student_DashBoard(request):
    return render(request, "wing_dashboard.html")

