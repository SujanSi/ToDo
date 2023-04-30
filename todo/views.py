from django.shortcuts import render,redirect
from .models import *

# Create your views here.


def index(request):
    employee=Employee.objects.all()
    context = {
        'employee': employee,
    }
    return render(request,'index.html',context)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        description = request.POST.get('description')
        a = Employee.objects.create(name=name,description=description)
        return redirect('index')
    else:
        return render(request,'create.html')
    
def update(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        employee.name = name
        employee.description = description
        employee.save()
        return redirect('index')
    else:
        return render(request, 'update.html', {'employee': employee})
    
def delete(request,employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    return redirect('index')