from django.db import models

# Create your models here.


class Users(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    resume = models.FilePathField(path='user_resumes')


class Company(models.Model):
    c_name = models.CharField(max_length=200)
    c_address = models.CharField(max_length=200)
    c_email = models.EmailField(max_length=100)
    c_country = models.CharField(max_length=200)
    c_type = models.CharField(max_length=200)
    c_contact = models.IntegerField()
    c_url = models.URLField()
    c_logo = models.ImageField(upload_to='company_logo', default='null')
