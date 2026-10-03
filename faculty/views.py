from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from faculty import models

def home(request):
    info = models.MainPageInfo.objects.first()
    return render(request, "faculty/home.html", {
        "info": info
    })

def programs(request):
    programs = models.Program.objects.select_related("department").all()
    return render(request, "faculty/programs.html", {
        "programs": programs
    })

def program_details(request, id):
    program = get_object_or_404(models.Program.objects.select_related("department"), pk=id)
    return render(request, "faculty/program_details.html", {
        "program": program
    })

def departments(request):
    departments = models.Department.objects.prefetch_related("programs").all()
    return render(request, "faculty/departments.html", {
        "departments": departments
    })

def department_detail(request, id):
    department = get_object_or_404(models.Department.objects.prefetch_related("programs", "lecturers"), pk=id)
    return render(request, "faculty/department_details.html", {
        "department": department
    })
