from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Import All the Forms and Models
from admin_panel.models import *
from students_panel.models import *


from .models import *
from .forms import *



# function for Creating A Outreach Model
@login_required
def Add_Programes(request):

    if not request.user.is_staff:
        messages.error(request, "You have not Access this, It is Only for Wing's Users... ")
        logout(request)
        return redirect("login_view")


    if request.method == 'POST':
            # Updating the Wing Model
        wing_Objt = Wing_Model.objects.get(wing_user = request.user)




        # Geting the UserName(Linked-in ot User) who is Posting the Programes

        # SubMitting the OutReach Form 
        Programe_Objt = Add_Program_Form(request.POST, request.FILES)

        # Preventing for Duplicate Program Code
        program_code = request.POST.get("Program_Code")
        if Program_Bank.objects.filter(Program_Code=program_code).exists():
            messages.error(request, "This Program already exists.")
            return render(request, "addProg.html", {"form": Programe_Objt})
        
        

        if Programe_Objt.is_valid():
            new_Registered = Programe_Objt.save(commit=False)

            new_Registered.Program_Created = wing_Objt
            new_Registered.save()

            if wing_Objt.Total_Registered == None:
                wing_Objt.Total_Registered = 0
                wing_Objt.save()

            else:
                wing_Objt.Total_Registered += 1 
                wing_Objt.save()
            
            new_Registered.save()
            wing_Objt.save()
            return redirect("Wing_DashBoard")
        else:
            Programe_Objt = Add_Program_Form()

            messages.error(request ,"Programe Not Registered .......")
            return render(request, "addProg.html", {"form" : Programe_Objt})

    else:
        Programe_Objt = Add_Program_Form()

    return render(request, "addProg.html", {"form" : Programe_Objt})





@login_required
def Register_StudentToPrograme(request):

    all_Programes = Program_Bank.objects.all()
    all_Students = Student_Model.objects.all()

     # Preventing for other User except of Students
    if request.user.is_superuser or  request.user.is_staff:
        messages.error(request, "You are a Student User, It is Only for Students's Users... ")
        logout(request)
        return redirect("login_view")


    if request.method == 'POST':

        newRegistration = Candidate_Registration_Form(request.POST)
        program_id = request.POST.get("program")

        stn_Objt = Student_Model.objects.get(user_Stn=request.user)
        To_Reg_Programe = Program_Bank.objects.get(id=program_id)

        # Prevent double registration
        if Candidates_Registration_Model.objects.filter(
            Candidates_Name=stn_Objt,
            Registered_Programe=To_Reg_Programe
        ).exists():
            messages.error(request, "You are already registered for this program.")
            return render(request, 'candidate.html', {
                "form": newRegistration,
                "all_Programes": all_Programes,
                "all_Students": all_Students,
            })

        # Updating total registrations in Program_Bank
        if To_Reg_Programe.Tatal_Registrations is None:
            To_Reg_Programe.Tatal_Registrations = 0
            To_Reg_Programe.save()


        #  error for Off Registration
        if not To_Reg_Programe.is_Registration:
            messages.error(request, "Registration is closed for this program.")
            return render(request, 'candidate.html', {
                "form": newRegistration,
                "all_Programes": all_Programes,
                "all_Students": all_Students,
            })
        
        if newRegistration.is_valid():
            Registered = newRegistration.save(commit=False)
            Registered.Candidates_Name = stn_Objt
            Registered.Registered_Programe = To_Reg_Programe
            Registered.save()


            To_Reg_Programe.Tatal_Registrations += 1

            # FOR THE Student WHO IS REGISTERING
            if stn_Objt.Total_Registered == None:
                stn_Objt.Total_Registered = 0
            
            if stn_Objt.Total_ClassProgrames == None:
                stn_Objt.Total_ClassProgrames = 0
            
            stn_Objt.Total_Registered += 1
            stn_Objt.Total_ClassProgrames += 1

            stn_Objt.save()
            To_Reg_Programe.save()

            messages.success(request, "Your Registration SuccessFully Done...")
            return redirect("Student_DashBoard")
        else:
            messages.error(request, "Candidate Not Registered.......")
            return render(request, 'candidate.html', {
                "form": newRegistration,
                "all_Programes": all_Programes,
                "all_Students": all_Students,
            })

    else:
        newRegistration = Candidate_Registration_Form()

    return render(request, 'candidate.html', {
        "form": newRegistration,
        "all_Programes": all_Programes,
        "all_Students": all_Students,
    })

# A = 5, B = 3
# 1 = 5, 2 = 3, 3 = 1 

def Mark_Distribution(position, grade):
    # for First with Grade Marking 
    if position == 1:
        if grade == "A Grade":
            return 10
        elif grade == "B Grade":
            return 8
        else:
            return 5

        
    # For Second 
    if position == 2:
        if grade == "A Grade":
            return 8
        elif grade == "B Grade":
            return 6
        else:
            return 3

        
    # for third 
    if position == 3:
        if grade == "A Grade":
            return 6
        elif grade == "B Grade":
            return 4
        else:
            return 1
    
    # only for A grade
    if grade == "A Grade":
        return 5
    elif grade == "B Grade":
        return 3
    else:
        return 0



@login_required
def Upload_Result(request, programe_name):
    if request.user.is_superuser or not request.user.is_staff:
        messages.error(request, "You have no access, it is only for Wing Users...")
        logout(request)
        return redirect("login_view")

        
    wing_Ojt = Wing_Model.objects.get(wing_user=request.user)
    Selected_Programe = Program_Bank.objects.get(Program_name =programe_name)

    all_Candidates = Candidates_Registration_Model.objects.filter(
        Registered_Programe=Selected_Programe
    )
    
    if request.method == 'POST':

        wing_Ojt = Wing_Model.objects.get(wing_user=request.user)
        Selected_Programe = Program_Bank.objects.get(Program_name=programe_name)
        Result_Objt = Upload_Result_Form(request.POST, request.FILES)

        # StudentS name 
        student_Objt = Student_Model.objects.all()

        # Candidate Position Holders
        Position_Holder1_id = request.POST.get("Position_Holder1")
        Position_Holder2_id = request.POST.get("Position_Holder2")
        Position_Holder3_id = request.POST.get("Position_Holder3")


        Grande_Holder1 = request.POST.get("Position_Holder1_Grade")
        Grande_Holder2 = request.POST.get("Position_Holder2_Grade")
        Grande_Holder3 = request.POST.get("Position_Holder3_Grade")

        Other_Grade_Holder  = request.POST.get("Grande_Holder")
        Other_Grade_Holder_Grade  = request.POST.get("Secure_Grade")
        
        print("Befor Validation Entry......")
        if Result_Objt.is_valid():
            print("Entered Validation Entry......")

            # Saving the Result Object
            Result_Objt = Result_Objt.save(commit=False)
            Result_Objt.Result_Uploaded_By = wing_Ojt
            Result_Objt.Result_Programe = Selected_Programe

            # Assign Candidate Objects
            Result_Objt.Position_Holder1 = Candidates_Registration_Model.objects.get(id = Position_Holder1_id)
            Result_Objt.Position_Holder2 = Candidates_Registration_Model.objects.get(id = Position_Holder2_id)
            Result_Objt.Position_Holder3 = Candidates_Registration_Model.objects.get(id = Position_Holder3_id)

            Result_Objt.Position_Holder1_Grade = Grande_Holder1
            Result_Objt.Position_Holder2_Grade = Grande_Holder2
            Result_Objt.Position_Holder3_Grade = Grande_Holder3

            # Other grade holder optional 
            if Other_Grade_Holder:
                Result_Objt.Grande_Holder = Candidates_Registration_Model.objects.get(id = Other_Grade_Holder)
                Result_Objt.Secure_Grade = Other_Grade_Holder_Grade

            # Position Marks 

            Result_Objt.Position_Holder1_Mark = Mark_Distribution(1, Grande_Holder1)
            Result_Objt.Position_Holder2_Mark = Mark_Distribution(2, Grande_Holder2)
            Result_Objt.Position_Holder3_Mark = Mark_Distribution(3, Grande_Holder3)

            print("All settuped  Validation Entry......")

            Result_Objt.save()

            # all marks 
            M1 = Mark_Distribution(1, Grande_Holder1)
            M2 = Mark_Distribution(2, Grande_Holder2)
            M3 = Mark_Distribution(3, Grande_Holder3)
            only_Grade = Mark_Distribution(0, Other_Grade_Holder_Grade)
            #assing mark for the student 

            # 1st Position Student
            holder_One = Result_Objt.Position_Holder1.Candidates_Name
            holder_One.Tatal_Points += M1
            holder_One.Total_ClassProgramesPoints += M1
            holder_One.Total_ReSulted += 1
            holder_One.save()

            # 2nd Position Student
            holder_Two = Result_Objt.Position_Holder2.Candidates_Name
            print(f"candidate name is : {holder_One.Student_Name}")
            holder_Two.Tatal_Points += M2
            holder_Two.Total_ClassProgramesPoints += M2
            holder_One.Total_ReSulted += 1
            holder_Two.save()

            # 3rd Position Student 
            holder_Three = Result_Objt.Position_Holder3.Candidates_Name
            holder_Three.Tatal_Points += M3
            holder_Three.Total_ClassProgramesPoints += M3
            holder_One.Total_ReSulted += 1
            holder_Three.save()


            # Grade Holder 
            only_Grade_Holder = Result_Objt.Grande_Holder.Candidates_Name
            only_Grade_Holder.Tatal_Points += only_Grade
            only_Grade_Holder.Total_ClassProgramesPoints += only_Grade
            only_Grade_Holder.Total_ReSulted += 1
            only_Grade_Holder.save()

            # how to assing this mark to the student
            
            # Some Validation After Result
            Selected_Programe.is_Registration = False
            Selected_Programe.is_Resulted = True
           
            Selected_Programe.save()

            messages.success(request, "Result Uploaded Successfully!")
            return redirect("Wing_DashBoard")

        else:
            messages.error(request, "Error in uploading result. Please check the form.")
            Result_Objt = Upload_Result_Form()
            context = {
            "Selected_Programe": Selected_Programe,
            "all_Candidates": all_Candidates,
            "form"  : Result_Objt
            }
            return render(request, "UploadResult.html", context)
    else:
        Result_Objt = Upload_Result_Form()

    context = {
        "Selected_Programe": Selected_Programe,
        "all_Candidates": all_Candidates,
        "form"  : Result_Objt
    }
    return render(request, "UploadResult.html", context)



@login_required
def Select_Programe_ForResult(request):
    wing_Ojt = Wing_Model.objects.get(wing_user=request.user)
    all_Programes = Program_Bank.objects.filter(Program_Created=wing_Ojt)

    return render(request, "Select_Programe.html", {"all_Programes": all_Programes})

@login_required
def Registrations_On_Off(request, programe_id):

    # Allow only staff users
    if not request.user.is_staff:
        messages.error(request, "You Have no access...")
        logout(request)
        return redirect("login_view")

    # Get program
    program = Program_Bank.objects.get(id=programe_id)

    # Toggle ON/OFF
    if program.is_Registration:
        program.is_Registration = False
    else:
        program.is_Registration = True

    program.save()


    # Message
    if program.is_Registration:
        messages.success(request, "Registration OPEN!")
    else:
        messages.success(request, "Registration CLOSE!")

        # if Admin close the Registration then to admin dashboard
    
    if request.user.is_superuser:
        return redirect("Admin_DashBoard")
    else:
        return redirect("Wing_DashBoard")

@login_required
def Direct_To_Upload_Result(request, programe_id):
    wing_Ojt = Wing_Model.objects.get(wing_user=request.user)
    Selected_Programe = Program_Bank.objects.get(id=programe_id)

    return redirect("Upload_Result", programe_name=Selected_Programe.Program_name)

@login_required
def View_Programe_Results(request, programe_id):
    wing_Ojt = Wing_Model.objects.get(wing_user=request.user)
    Selected_Programe = Program_Bank.objects.get(id=programe_id)

    Result_Objt = Result_Bank_Model.objects.filter(
        Result_Programe=Selected_Programe
    ).first()

    context = {
        "Selected_Programe": Selected_Programe,
        "Result_Objt": Result_Objt
    }

    return render(request, "ViewResults.html", context)


