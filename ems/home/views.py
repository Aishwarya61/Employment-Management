from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Employee,Role,Department
from .form import EmployeeForm
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,'index.html')

def add_emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
          employee = form.save(commit = False)  
          employee.hire_date = date.today()
          employee.save()
          return redirect('home:all_emp')
    else:
        form = EmployeeForm()
    return render(request,'add_emp.html',{'form':form})

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            removed_emp = Employee.objects.get(id=emp_id)
            removed_emp.delete()
            return redirect('home:all_emp')
        except:
            return HttpResponse("Some Error Occured")
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'all_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name)| Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains =role)
        context = {
            'emps':emps,
            'name': name,  
            'dept': dept,
            'role': role,
        }
        return render(request,'all_emp.html',context)
    
    else:
        return render(request,'filter_emp.html')