from django.shortcuts import render
from django.http import HttpResponse

def empty(request):
    return HttpResponse("empty view")

def programs(request):
    return HttpResponse("programs view")

def program_details(request, id):
    return HttpResponse("details for a specific program")

def departments(request):
    return HttpResponse("departments view")

def department_detail(request, id):
    return HttpResponse("details for a specific department")
