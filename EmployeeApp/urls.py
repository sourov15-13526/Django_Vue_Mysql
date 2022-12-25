from django.urls import path
from EmployeeApp import views


urlpatterns = [
    path('department/',views.departmentApi),
    path('employee/',views.employeeApi)
]
