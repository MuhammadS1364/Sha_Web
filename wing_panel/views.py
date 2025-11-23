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
    if request.method == 'POST':
        newRegistration = Candidate_Registration_Form(request.POST)
        program_id = request.POST.get("program")

        # secure the doubble registration , a student can not register for the same program twice
        if Candidates_Registration_Model.objects.filter(
            Candidates_Name=request.user,
            Registered_Programe= program_id
        ).exists():
            messages.error(request, "You are already registered for an active program.")
            return render(request, 'candidate.html', {
        "form": newRegistration,
        "all_Programes": all_Programes,
        "all_Students" : all_Students,
    })
        # Filter active programs

        
        To_Reg_Programe = Program_Bank.objects.get(id = program_id)

        if all_Programes.filter(id=program_id).exists():
            messages.success(request, "You are registered for the program.")
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


def Upload_Result(request, programe_id):
    wing_Ojt = Wing_Model.objects.get(wing_user=request.user)
    Selected_Programe = Program_Bank.objects.get(id=programe_id)

    all_Candidates = Candidates_Registration_Model.objects.filter(
        Registered_Programe=Selected_Programe
    )
    
    if request.method == 'POST':

        wing_Ojt = Wing_Model.objects.get(wing_user=request.user)
        Selected_Programe = Program_Bank.objects.get(id=programe_id)
        Result_Objt = Upload_Result_Form(request.POST, request.FILES)

        if Result_Objt.is_valid():

            # Saving the Result Object
            Result_Objt = Result_Objt.save(commit=False)
            Result_Objt.Result_Uploaded_By = wing_Ojt
            Result_Objt.Result_Programe = Selected_Programe

            # Candidate Position Holders
            Position_Holder1_id = request.POST.get("Position_Holder1")
            Position_Holder2_id = request.POST.get("Position_Holder2")
            Position_Holder3_id = request.POST.get("Position_Holder3")

            # Candidate img 
            Position_Holder1_img = request.FILES.get("Position_Holder1_img")
            Position_Holder2_img = request.FILES.get("Position_Holder2_img")
            Position_Holder3_img = request.FILES.get("Position_Holder3_img")
            
            Grande_Holder = request.POST.get("Grande_Holder")

            # setting the position holders
            Result_Objt.Position_Holder1 = Position_Holder1_id
            Result_Objt.Position_Holder2 = Position_Holder2_id
            Result_Objt.Position_Holder3 = Position_Holder3_id

            # setting the position holder images
            Result_Objt.Position_Holder1_img = Position_Holder1_img
            Result_Objt.Position_Holder2_img = Position_Holder2_img
            Result_Objt.Position_Holder3_img = Position_Holder3_img

            # setting the Grande Holder
            Result_Objt.Grande_Holder = Grande_Holder
            Result_Objt.save()
            messages.success(request, "Result Uploaded Successfully!")
            return redirect("Wing_DashBoard")

        else:
            messages.error(request, "Error in uploading result. Please check the form.")
            Result_Objt = Upload_Result_Form()
            return render(request, "UploadResult.html", context)
    else:
        Result_Objt = Upload_Result_Form()
    context = {
        "Selected_Programe": Selected_Programe,
        "all_Candidates": all_Candidates,
        "form"  : Result_Objt
    }
    return render(request, "UploadResult.html", context)


def Select_Programe_ForResult(request):
    wing_Ojt = Wing_Model.objects.get(wing_user=request.user)
    all_Programes = Program_Bank.objects.filter(Program_Created=wing_Ojt)

    return render(request, "Select_Programe.html", {"all_Programes": all_Programes})
