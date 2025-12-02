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
from django.urls import path, include
from admin_panel import views

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler404, handler500
urlpatterns = [
    path('admin/', admin.site.urls, name="Main_admin"),


    path('student-panel/', include("students_panel.urls")),
    path('wing-panel/', include("wing_panel.urls")),

    

    # Entery and Exit Functions 
    path('', views.login_view, name="login_view"),
    path('log-out/', views.logout_view, name="logout_view"),


    # Adding New Users , Students , and Wings 
    path('newUser/', views.newUser, name="newUser"),
    path('addStn/', views.add_student, name="add_student"),
    path('addWing/', views.add_wing, name="add_wing"),


    # Dash Board Views 
    path('admin-dash/', views.Admin_DashBoard, name="Admin_DashBoard"),
    path('wing-dash/', views.Wing_DashBoard, name="Wing_DashBoard"),
    path('student-dash/', views.Student_DashBoard, name="Student_DashBoard"),

    # edite functions 
    path('pass/', views.editePassword, name="editePassword"),
    # path('pass/', views.editePassword, name="editePassword"),
    path('print-reults/', views.export_result_excel, name="export_result_excel"),
    path('print-programes/', views.Export_Programes, name="Export_Programes"),


    # Test Paths 
    # path('admin-test-dash/', views.Admin_TestBoard, name="Admin_TestBoard"),
    path('wing-test-dash/', views.Wing_TestBoard, name="Wing_TestBoard"),
    # path('stn-dir/', views.new_Student, name="new_Student"),
    path('student-test-dash/', views.Student_TestBoard, name="Student_TestBoard"),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

