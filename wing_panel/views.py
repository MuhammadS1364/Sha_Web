from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages



# Import All the Forms and Models
from admin_panel.models import *
from students_panel.models import *


from .models import *
from .forms import *



# function for Creating A Outreach Model

def Add_Programes(request):
    
    if request.method == 'POST':

        # Geting the UserName(Linked-in ot User) who is Posting the Programes
        wing_Objt = Wing_Model.objects.get(wing_user = request.user)

        # SubMitting the OutReach Form 
        Programe_Objt = Add_Program_Form(request.POST, request.FILES)

        if Programe_Objt.is_valid():
            new_Registered = Programe_Objt.save(commit=False)

            new_Registered.Program_Created = wing_Objt
            new_Registered.save()

            return redirect("Wing_DashBoard")
        else:
            Programe_Objt = Add_Program_Form()

            messages.error("Programe Not Registered .......")
            return render(request, "addProg.html", {"form" : Programe_Objt})

    else:
        Programe_Objt = Add_Program_Form()

    return render(request, "addProg.html", {"form" : Programe_Objt})




def Register_StudentToPrograme(request):
    all_Programes = Program_Bank.objects.all()
    all_Students = Student_Model.objects.all()

    # To_Be_Registered = None
    # for programe in all_Programes:
    #     To_Reg_Programe = programe
    


    if request.method == 'POST':
        newRegistration = Candidate_Registration_Form(request.POST)

        program_id = request.POST.get("program")
        To_Reg_Programe = Program_Bank.objects.get(id = program_id)

        stn_Objt = Student_Model.objects.get(user_Stn=request.user)
        
        if newRegistration.is_valid():
            Registered = newRegistration.save(commit=False)
            Registered.Candidates_Name = stn_Objt
            Registered.Registered_Programe = To_Reg_Programe
            Registered.save()

            # students save karna:
            newRegistration.save()

            return redirect("Student_DashBoard")
        else:
            messages.error("Candidate Not Registered.......")
            return render(request, 'candidate.html', {
        "form": newRegistration,
        "all_Programes": all_Programes,
        "all_Programes" : all_Programes
        })


    else:
        newRegistration = Candidate_Registration_Form()

    return render(request, 'candidate.html', {
        "form": newRegistration,
        "all_Programes": all_Programes,
        "all_Students" : all_Students,
    })


# def Upload_Result(request,programe_id):

#     wing_Ojt = Wing_Model.objects.get(wing_user = request.user)
#     Selected_Programe = Program_Bank.objects.get(id= programe_id)

#     all_Candidates = Candidates_Registration_Model.objects.filter(
#         Registered_Programe = Selected_Programe
#     )

#         # Ready_To_Upload = None

  
#     context = {
#         "all_Programes" : Selected_Programe,
#         "all_Candidates" : all_Candidates
#     }
#     return render(request, "UploadResult.html", context)

def Upload_Result(request, programe_id):
    wing_Ojt = Wing_Model.objects.get(wing_user=request.user)
    Selected_Programe = Program_Bank.objects.get(id=programe_id)

    all_Candidates = Candidates_Registration_Model.objects.filter(
        Registered_Programe=Selected_Programe
    )
    
    if request.method == 'POST':
        Result_Objt = Upload_Result_Form(request.POST, request.FILES)

        if Result_Objt.is_valid():
            pass
    else:
        Result_Objt = Upload_Result_Form()
    context = {
        "Selected_Programe": Selected_Programe,
        "all_Candidates": all_Candidates,
        "form"  : Result_Objt
    }
    return render(request, "UploadResult.html", context)


# def Select_Programe_ForResult(request):

#     wing_Ojt = Wing_Model.objects.get(wing_user = request.user)
#     all_Programes = Program_Bank.objects.filter(Program_Created = wing_Ojt)

#     if request.method == 'POST':
#         return redirect("Upload_Result")

#     return render(request, "Select_Programe.html", {"all_Programes": all_Programes})



def Select_Programe_ForResult(request):
    wing_Ojt = Wing_Model.objects.get(wing_user=request.user)
    all_Programes = Program_Bank.objects.filter(Program_Created=wing_Ojt)

    return render(request, "Select_Programe.html", {"all_Programes": all_Programes})
