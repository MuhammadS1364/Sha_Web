"""
URL configuration for shaad_maan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from admin_panel import views
urlpatterns = [
    path('admin/', admin.site.urls),


    # Entery and Exit Functions 
    path('log-in/', views.login_view, name="login_view"),
    path('log-out/', views.logout_view, name="logout_view"),


    # Adding New Users , Students , and Wings 
    path('newUser/', views.newUser, name="newUser"),
    path('addStn/', views.add_student, name="add_student"),
    path('addWing/', views.add_wing, name="add_wing"),


    # Dash Board Views 
    path('admin-dash/', views.Admin_DashBoard, name="Admin_DashBoard"),
    path('wing-dash/', views.Wing_DashBoard, name="Wing_DashBoard"),
    path('student-dash/', views.Student_DashBoard, name="Student_DashBoard"),

]
