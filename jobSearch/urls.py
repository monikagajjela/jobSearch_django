from django.urls import path
from . import views as auth_views

urlpatterns = [
    path('index/', auth_views.index, name=''),
    path('about', auth_views.about, name='about'),
    path('jobdetails', auth_views.jobdetails, name='jobdetails'),
    path('joblisting', auth_views.joblisting, name='joblisting'),
    path('contact', auth_views.contact, name='contact'),
    path('userRegister', auth_views.userRegister, name='userRegister'),
    path('employeeReg', auth_views.employeeReg, name='employeeReg'),
    path('elogin', auth_views.employeeLogin, name='elogin'),
    path('ulogin', auth_views.userLogin, name='ulogin'),

]
