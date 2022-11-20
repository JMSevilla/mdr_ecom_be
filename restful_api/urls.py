from django.urls import re_path, path
from restful_api.Controller.BusinessOwner import BOController, ProjectController
from restful_api.Controller.Service import LoginController, TokenController
from restful_api.Controller.Service.Contact import ContactController
from restful_api.Controller.Administrator import AdminController
from restful_api.Controller.Student.studentController import StudentController
from restful_api.Controller.Service.SignoutController import SignoutController
from restful_api.Controller.Product.ProductController import ProductsController
from restful_api.Controller.Administrator.TrainingController import TrainingController

urlpatterns = [
    re_path(
        r'^api/checkowner/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', BOController.BusinessOwnerController.checkemail),
    re_path(r'^api/businessowner/registration/$',
            BOController.BusinessOwnerController.businessowner_registration),
    re_path(r'^api/project/$', ProjectController.ProjectController.projectEntry),
    re_path(r'^api/business-checkemail/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<code>[\w\-]+)/$',
            BOController.BusinessOwnerController.business_verification),
    re_path(r'^api/verification-entry$',
            BOController.BusinessOwnerController.business_verification_record),
    re_path(
        r'^api/check-email-counts/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<code>[\w\-]+)/$', BOController.BusinessOwnerController.business_verification_checkcounts),
    # re_path(r'^api/check-before-sending/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',
    #         BOController.BusinessOwnerController.business_check_beforesend),
    re_path(r'^api/check-email-verification/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',
            BOController.BusinessOwnerController.business_verify_email),
    re_path(r'^api/business-update-with-send/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<code>[\w\-]+)/$',
            BOController.BusinessOwnerController.business_update_with_sendemail),
    re_path(r'^api/compare-verification-code/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<code>[\w\-]+)/$',
            BOController.BusinessOwnerController.compare_verification_code),
    re_path(r'^api/project-creation/$',
            ProjectController.ProjectController.create_project),
    # fetching api project and business owner
    re_path(r'^api/getall-projectbyemail/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',
            ProjectController.ProjectController.__fetch_project__),
    re_path(r'^api/getall-businessbyemail/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',
            BOController.BusinessOwnerController.findAllBo),
    re_path(r'^api/applogin$', LoginController.login),
    re_path(r'^api/get-token$',
            TokenController.TokenizationController.tokenIdentify),
    re_path(r'^api/send-message/contactus$',
            ContactController.ContactController.sendMessage),
    re_path(r'^api/check-admin$',
            AdminController.AdministratorController.check_admin_controller),
    re_path(r'^api/admin-registration-entry$',
            AdminController.AdministratorController.admin_registration_controller),
    re_path(r'^api/signup-config-check-email/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',
            BOController.BusinessOwnerController.configAPI_checkemail),
    re_path(
        r'^api/student-check-email/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',
        StudentController.studentCheckEmail),
    re_path(
        r'^api/student-verification-counts-before-update/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<code>[\w\-]+)/$',
        StudentController.student_verification_checkcounts),
    re_path(
        # r'^api/signout/(?P<userid>\d+)/(?P<token>[\w\-]+)/$',
        r'^api/signout/$',
        SignoutController.signout
    ),
    re_path(r'^api/signout_bo/$',
        SignoutController.signout),
    re_path(r'^api/signout_st/$',
        SignoutController.signout_st),
    re_path(r'^api/student-check-verification/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',
            StudentController.student_verify_email),
    re_path(r'^api/student-verification-entry$',
            StudentController.student_verification_record),
    re_path(r'^api/student-verification-send-email/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<code>[\w\-]+)/$',
            StudentController.student_verification),
    re_path(r'^api/student-verification-sent-count-update/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<code>[\w\-]+)/$',
            StudentController.student_update_with_sendemail),
        re_path(r'^api/tokenization/check-secure-route$', TokenController.route_token_checker),
        re_path(r'^api/product-category/add$', ProductsController.addProjectCategories),
        re_path(r'^api/product-category/all', ProductsController.getAllProjectCategories),
        re_path(r'^api/product-category/delete-category/(\d+)/$', ProductsController.removeProjectCategories),
        re_path(r'^api/administrator/training-add$', TrainingController.addTraining),
        re_path(r'^api/get-all-trainings$', TrainingController.getAllTrainings),
        re_path(r'^api/training-management/edit-trainings$', TrainingController.editTrainings),
        re_path(r'^api/training-management/delete/(\d+)/$', TrainingController.removeTraining)
]
