from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def jobdetails(request):
    return render(request, 'job_details.html')


def joblisting(request):
    return render(request, 'job_listing.html')


def employeeReg(request):
    return render(request, 'Employee/EmployeeReg.html')


def userRegister(request):
    return render(request, 'User/userRegistration.html')


def employeeLogin(request):
    return render(request, 'Employee/EmployeeLogin.html')


def userLogin(request):
    return render(request, 'User/userLogin.html')
