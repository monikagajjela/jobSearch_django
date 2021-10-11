from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('jobdetails', views.jobdetails, name='jobdetails'),
    path('joblisting', views.joblisting, name='joblisting'),
    path('contact', views.contact, name='contact'),
    path('userRegister', views.userRegister, name='userRegistration'),
    path('employeeReg', views.employeeReg, name='employeeReg'),

]
