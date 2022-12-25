from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    
    elif request.method=='POST':  # Post method will insert new records
        department_data=JSONParser().parse(request)  # allow you to accept requests with various media types
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Succesfully",safe=False)
        return JsonResponse('Failed to Add', safe=False)
    
    elif request.method=='PUT':  # put mathod will update a given record
        department_data=JSONParser().parse(request) # allow you to accept requests with various media types
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Fail to Update")
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    
        
@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employee_serializer = EmployeeSerializer(employees,many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer=EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Succesfully",safe=False)
        return JsonResponse('Failed to Add', safe=False)
    
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees.objects.get(Employee=employee_data['EmployeeId'])
        employee_serializer=EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Fail to Update")
    elif request.method=='DELETE':
        employee=Employees.objects.get(Employee=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)
