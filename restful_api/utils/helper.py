from restful_api.models import BusinessOwner
from restful_api.models import Project
from django.contrib.auth.hashers import make_password
from restful_api.models import AccountVerification_1
from django.db.models import F


class GeneralParams:
    params_result = ''
    field_success_BO_registration = ''
    field_success_Project_entry = ''
    field_verification_bo = ''
    field_check_counts = []
    field_update_counts = ''
    field_check_code_inputs = []
    field_email_checker_str = ''


class GeneralHelper:
    def Slug(method, condition, params):
        match method:
            case 'GET':
                if condition == 'api/checking-email':
                    return GeneralHelper.checkEmail(params)
                elif condition == 'business-verification-check-counts':
                    return GeneralHelper.__init__vrfy_check_counts(params)
                elif condition == 'business-verification-check-code':
                    return GeneralHelper.__init__check_code_inputs(params)
                elif condition == 'business-check-email-verification':
                    return GeneralHelper.__init__check_email_before_push(params)
            case 'POST':
                if condition == 'api/business-owner-registration':
                    return GeneralHelper.__init__registration_businessowner(params)
                elif condition == 'api/project-entry':
                    return GeneralHelper.__init__project_entry(params)
                elif condition == 'business-verification-dbentry':
                    return GeneralHelper.__init__verification_entry(params)
            case 'PUT':
                if condition == 'api/business-update-counts':
                    return GeneralHelper.__init__update_counts(params)

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

    def __init__vrfy_check_counts(params):
        scan_counts = AccountVerification_1.objects.filter(
            client_email=params
        ).filter(sent_count=3).values()
        GeneralParams.field_check_counts = scan_counts
        return GeneralParams.field_check_counts

    def __init__update_counts(params):
        AccountVerification_1.objects.filter(
            client_email=params['email']
        ).update(sent_count=F('sent_count')+1, verification_code=params['code'])
        GeneralParams.field_update_counts = "success"
        return GeneralParams.field_update_counts

    def __init__check_code_inputs(params):
        compared = AccountVerification_1.objects.filter(
            verification_code=params
        ).values()
        GeneralParams.field_check_code_inputs = compared
        return GeneralParams.field_check_code_inputs

    def __init__check_email_before_push(params):
        filtered = AccountVerification_1.objects.filter(
            client_email=params
        ).values()
        if filtered.count() > 0:
            onCount = AccountVerification_1.objects.filter(
                sent_count=3
            ).values()
            if onCount.count() > 0:
                GeneralParams.field_email_checker_str = "exceed_limit"
            else:
                GeneralParams.field_email_checker_str = "update_another_sent_count"
        else:
            GeneralParams.field_email_checker_str = "doest_not_exist"
        return GeneralParams.field_email_checker_str