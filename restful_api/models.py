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
    projectfeatures = models.CharField(max_length=255, blank=False, default='')
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
