from django.urls import path
from faculty import views

urlpatterns = [
    path("", views.empty, name="empty"),
    path("programs", views.programs, name="programs"),
    path("programs/<id>", views.program_details, name="program_details"),
    path("departments", views.departments, name="departments"),
    path("departments/<id>", views.department_detail, name="department_details")
]
