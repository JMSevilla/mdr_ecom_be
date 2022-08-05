from django.urls import re_path, path
from restful_api.Controller.BusinessOwner import BOController

urlpatterns = [
    re_path(r'^api/checkowner/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', BOController.checkemail),
    re_path(r'^api/businessowner/registration/$', BOController.businessowner_registration)
]