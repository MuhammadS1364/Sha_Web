from django.shortcuts import render

# Create your views here.

def login_view (request):
    if request.method == 'POST':
        userName = request.POST.get("username")
        userPass = request.POST.get("password")
        print(f"Your userName is ({userName}) and Password is: ({userPass})")

    return render(request, "login_user.html")