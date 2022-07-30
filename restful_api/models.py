from django.db import models

class Users(models.Model):
    firstname = models.CharField(max_length=100, blank=False, default='')
    lastname = models.CharField(max_length=100, blank=False, default='') 
    username = models.CharField(max_length=150, blank=False, default='') 
    email = models.EmailField() 
    password = models.CharField(max_length=255, blank=False, default='')
    userType = models.CharField(max_length=1, blank=False, default='')
    isLock = models.CharField(max_length=1, blank=False, default='')
    isverified = models.CharField(max_length=1, blank=False, default='')
    imgURL = models.CharField(max_length=255, blank=False, default='')
    role = models.CharField(max_length=100, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

