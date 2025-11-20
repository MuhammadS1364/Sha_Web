from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



# Import All the Forms and Models
from admin_panel.models import *
from students_panel.models import *


from .models import *
from .forms import *



# function for Creating A Outreach Model

def Add_Programes(request):
    
    if request.method == 'POST':

        # Geting the UserName(Linked-in ot User) who is Posting the Programes
        wing_Obj = Wing_Model.objects.get(wing_user = request.user)

        # SubMitting the OutReach Form 
        new_Progs_Obj = Add_Program_Form(request.POST, request.FILES)

        if new_Progs_Obj.is_valid():
            new_Register = new_Progs_Obj.save(commit=False)

            new_Register.program_Created = wing_Obj
            new_Register.save()

            return redirect("Wing_DashBoard")
        else:
            return HttpResponse("Programe Not Registered .......")
    else:
        new_Progs_Obj = Add_Program_Form()

    return render(request, "addProg.html", {"form" : new_Progs_Obj})


# def Register_StudentToPrograme(request):
#     all_Programes = Program.objects.all()

#     if request.method == 'POST':

#         newRegistration = Registration_Programe(request.POST , request.FILES)

#         Programe_iDS = request.POST.get("program_name")
#         To_Reg_Programe = Program.objects.get(id =Programe_iDS)

#         # which wing member register 
#         wing_Obj = Wing_Model.objects.get(wing_user = request.user)
        
#         if newRegistration.is_valid():
#             Registered = newRegistration.save(commit=False)
#             Registered.wing_name = wing_Obj
#             Registered.program = To_Reg_Programe
#             Registered.save()
#             return redirect("Wing_DashBoard")
#         else:
#             return HttpResponse("Candidate Not Registered.......")
#     else:
#         newRegistration = Registration_Programe()

#     return render(request, 'candidate.html', {
#         "form": newRegistration,
#         "all_Programes" : all_Programes
#         })

def Register_StudentToPrograme(request):
    all_Programes = Program.objects.all()

    if request.method == 'POST':
        print("POST DATA = ", request.POST)
        newRegistration = Registration_Programe(request.POST)

        program_id = request.POST.get("program")
        To_Reg_Programe = Program.objects.get(id = program_id)

        wing_Obj = Wing_Model.objects.get(wing_user=request.user)
        
        if newRegistration.is_valid():
            Registered = newRegistration.save(commit=False)
            Registered.wing_name = wing_Obj
            Registered.program = To_Reg_Programe
            Registered.save()

            # ManyToMany students save karna:
            newRegistration.save_m2m()

            return redirect("Wing_DashBoard")
        else:
            return HttpResponse("Candidate Not Registered.......")

    else:
        newRegistration = Registration_Programe()

    return render(request, 'candidate.html', {
        "form": newRegistration,
        "all_Programes": all_Programes
    })
