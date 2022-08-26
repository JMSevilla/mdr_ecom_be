from django.db import models

# class Users(models.Model):
#     firstname = models.CharField(max_length=100, blank=False, default='')
#     lastname = models.CharField(max_length=100, blank=False, default='')
#     username = models.CharField(max_length=150, blank=False, default='')
#     email = models.EmailField()
#     password = models.CharField(max_length=255, blank=False, default='')
#     userType = models.CharField(max_length=1, blank=False, default='')
#     isLock = models.CharField(max_length=1, blank=False, default='')
#     isverified = models.CharField(max_length=1, blank=False, default='')
#     imgURL = models.CharField(max_length=255, blank=False, default='')
#     role = models.CharField(max_length=100, blank=False, default='')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class BusinessOwner(models.Model):
    firstname = models.CharField(max_length=100, blank=False, default='')
    lastname = models.CharField(max_length=100, blank=False, default='')
    contactnumber = models.BigIntegerField()
    address = models.CharField(max_length=255, blank=False, default='')
    email = models.EmailField()
    password = models.CharField(max_length=255, blank=False, default='')
    userType = models.CharField(max_length=1, blank=False, default='')
    isLock = models.CharField(max_length=1, blank=False, default='')
    isverified = models.CharField(max_length=1, blank=False, default='')
    imgURL = models.CharField(max_length=255, blank=False, default='')
    sec_question = models.CharField(max_length=150, blank=False, default='')
    sec_answer = models.CharField(max_length=255, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Project(models.Model):
    projectname = models.CharField(max_length=155, blank=False, default='')
    projectdetails = models.CharField(max_length=255, blank=False, default='')
    projectcategory = models.CharField(max_length=100, blank=False, default='')
    projecttype = models.CharField(max_length=100, blank=False, default='')
    projectfeatures = models.TextField()
    projectprice = models.BigIntegerField()
    clientEmail = models.CharField(max_length=255, blank=False, default='')
    projectstatus = models.CharField(max_length=1, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AccountVerification_1(models.Model):
    client_email = models.EmailField()
    verification_code = models.CharField(
        max_length=255, blank=False, default='')
    verified = models.CharField(max_length=1, blank=False, default='')
    user_type = models.CharField(max_length=100, blank=False, default='')
    sent_count = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tokenization(models.Model):
    userID = models.BigIntegerField()
    token = models.CharField(max_length=255, blank=False, default='')
    lastRoute = models.CharField(max_length=100, blank=False, default='')
    isDestroyed = models.CharField(max_length=1, blank=False, default='')
    isvalid = models.CharField(max_length=1, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Student(models.Model):
    firstname = models.CharField(max_length=100, blank=False, default='')
    lastname = models.CharField(max_length=100, blank=False, default='')
    contactnumber = models.BigIntegerField()
    address = models.CharField(max_length=255, blank=False, default='')
    email = models.EmailField()
    password = models.CharField(max_length=255, blank=False, default='')
    userType = models.CharField(max_length=1, blank=False, default='')
    isLock = models.CharField(max_length=1, blank=False, default='')
    isverified = models.CharField(max_length=1, blank=False, default='')
    imgURL = models.CharField(max_length=255, blank=False, default='')
    sec_question = models.CharField(max_length=150, blank=False, default='')
    sec_answer = models.CharField(max_length=255, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StudentRequirements(models.Model):
    student_email = models.EmailField()
    req_studentIdFileURL = models.CharField(
        max_length=255, blank=False, default='')
    req_studentBirthCertURL = models.CharField(
        max_length=255, blank=False, default='')


class StudentDetails(models.Model):
    school = models.CharField(max_length=100, blank=False, default='')
    purpose = models.CharField(max_length=100, blank=False, default='')
    birthdate = models.DateField()
    studylevel = models.CharField(max_length=100, blank=False, default='')


class Administrator(models.Model):
    firstname = models.CharField(max_length=100, blank=False, default='')
    lastname = models.CharField(max_length=100, blank=False, default='')
    email = models.EmailField()
    password = models.CharField(max_length=255, blank=False, default='')
    userType = models.CharField(max_length=1, blank=False, default='')
    isLock = models.CharField(max_length=1, blank=False, default='')
    isverified = models.CharField(max_length=1, blank=False, default='')
    imgURL = models.CharField(max_length=255, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ContactUs(models.Model):
    fullname = models.CharField(max_length=255, blank=False, default='')
    email = models.EmailField()
    subject = models.CharField(max_length=150, blank=False, default='')
    message = models.TextField()