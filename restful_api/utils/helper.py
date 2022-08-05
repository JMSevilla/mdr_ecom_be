from restful_api.models import BusinessOwner
from restful_api.models import Project
from django.contrib.auth.hashers import make_password

class GeneralParams:
    params_result = ''
    field_success_BO_registration = ''
    

class GeneralHelper:
    def Slug(method, condition, params):
        match method:
            case 'GET':
                if condition == 'api/checking-email':
                    return GeneralHelper.checkEmail(params)
            case 'POST':
                if condition == 'api/business-owner-registration':
                    return GeneralHelper.__init__registration_businessowner(params)
    
    #entity functions
    def checkEmail(params):
        filtered = BusinessOwner.objects.filter(
            email=params
        ).values()
        if filtered.exists():
            GeneralParams.params_result = "email_taken"
        else:
            GeneralParams.params_result = "email_available"
        return GeneralParams.params_result

    def __init__registration_businessowner(params):
        businessowner = BusinessOwner()
        businessowner.firstname = params['firstname']
        businessowner.lastname = params['lastname']
        businessowner.contactnumber = params['contactnumber']
        businessowner.address = params['address']
        businessowner.email = params['email']
        businessowner.password = make_password(params['password'])
        businessowner.userType = "3"
        businessowner.isLock = "0"
        businessowner.isverified = params['isverified']
        businessowner.imgURL = "none"
        businessowner.save()
        GeneralParams.field_success_BO_registration = "success_bo_registration"
        return GeneralParams.field_success_BO_registration