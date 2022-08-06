from restful_api.models import BusinessOwner
from restful_api.models import Project
from django.contrib.auth.hashers import make_password
from restful_api.models import AccountVerification_1


class GeneralParams:
    params_result = ''
    field_success_BO_registration = ''
    field_success_Project_entry = ''
    field_verification_bo = ''


class GeneralHelper:
    def Slug(method, condition, params):
        match method:
            case 'GET':
                if condition == 'api/checking-email':
                    return GeneralHelper.checkEmail(params)
            case 'POST':
                if condition == 'api/business-owner-registration':
                    return GeneralHelper.__init__registration_businessowner(params)
                elif condition == 'api/project-entry':
                    return GeneralHelper.__init__project_entry(params)
                elif condition == 'business-verification-dbentry':
                    return GeneralHelper.__init__verification_entry(params)

    # entity functions
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

    def __init__project_entry(params):
        project = Project()
        project.projectname = params['projectname']
        project.projectdetails = params['projectdetails']
        project.projectfeatures = params['projectfeatures']
        project.projectprice = params['projectprice']
        project.projectstatus = "0"
        project.projecttype = params['projecttype']
        project.save()
        GeneralParams.field_success_Project_entry = "success_project_entry"
        return GeneralParams.field_success_Project_entry

    def __init__verification_entry(params):
        account_verification = AccountVerification_1()
        account_verification.client_email = params['email']
        account_verification.verification_code = params['code']
        account_verification.verified = "0"
        account_verification.user_type = "3"
        account_verification.sent_count = 1
        account_verification.save()
        GeneralParams.field_verification_bo = "success_vc_entry"
        return GeneralParams.field_verification_bo
