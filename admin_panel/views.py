from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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


def newUser (request):
    if request.method == 'POST':
        userName = request.POST.get("userName")
        userEmail = request.POST.get("userEmail")
        userPass = request.POST.get("userPass")
        userRole = request.POST.get("role")
        new_user = User.objects.create_user(
            username = userName, 
            email = userEmail,
            password = userPass
        )
        new_user.save()
        if userRole == "Admin":
            new_user.is_superuser = True
            new_user.is_staff = True

        elif userRole == 'Wing':
            new_user.is_staff = True

        else:
            new_user.is_superuser = False
            new_user.is_staff = False
            
        new_user.save()

        return HttpResponse("yes user created........")
    return render(request, "addUser.html")

from .forms import *

def add_student(request):
    if request.method == 'POST':

        new_stn_form = Student_form(request.POST,request.FILES )

        if new_stn_form.is_valid():
            new_stn_form.save()
            return HttpResponse("Student Added.........")
        else:
            return HttpResponse("Student Not Added.........")
    else:
        new_stn_form = Student_form()
    return render(request, 'addUser.html', {"form": new_stn_form})
