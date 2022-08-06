from django.urls import re_path, path
from restful_api.Controller.BusinessOwner import BOController, ProjectController

urlpatterns = [
    re_path(r'^api/checkowner/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', BOController.BusinessOwnerController.checkemail),
    re_path(r'^api/businessowner/registration/$', BOController.BusinessOwnerController.businessowner_registration),
    re_path(r'^api/project/$', ProjectController.ProjectController.projectEntry)
]   