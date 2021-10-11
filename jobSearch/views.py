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
    return render(request, 'EmployeeReg.html')


def userRegister(request):
    return render(request, 'userRegistration.html')
