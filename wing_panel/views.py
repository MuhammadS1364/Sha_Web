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
        stn_Objt = Wing_Model.objects.get(wing_user = request.user)

        # SubMitting the OutReach Form 
        Programe_Objt = Add_Program_Form(request.POST, request.FILES)

        if Programe_Objt.is_valid():
            new_Registered = Programe_Objt.save(commit=False)

            new_Registered.Program_Created = stn_Objt
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

    if request.method == 'POST':
        newRegistration = Candidate_Registration_Form(request.POST)

        program_id = request.POST.get("program")
        To_Reg_Programe = Program_Bank.objects.get(id = program_id)

        stn_Objt = Student_Model.objects.get(user_Stn=request.user)
        
        if newRegistration.is_valid():
            Registered = newRegistration.save(commit=False)
            Registered.user_Stn = stn_Objt
            Registered.Registered_Programe = To_Reg_Programe
            Registered.save()

            # students save karna:
            newRegistration.save()

            return redirect("Wing_DashBoard")
        else:
            messages.error("Candidate Not Registered.......")
            return render(request, 'candidate.html', {
        "form": newRegistration,
        "all_Programes": all_Programes
        })


    else:
        newRegistration = Candidate_Registration_Form()

    return render(request, 'candidate.html', {
        "form": newRegistration,
        "all_Programes": all_Programes
    })
