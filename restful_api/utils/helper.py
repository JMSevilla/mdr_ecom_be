import string
import random
from restful_api.models import Administrator, BusinessOwner, Student, Tokenization
from restful_api.models import Project
from django.contrib.auth.hashers import make_password
from restful_api.models import AccountVerification_1
from django.db.models import F
from django.contrib.auth.hashers import check_password


class GeneralParams:
    params_result = ''
    field_success_BO_registration = ''
    field_success_Project_entry = ''
    field_verification_bo = ''
    field_check_counts = []
    field_update_counts = ''
    field_check_code_inputs = []
    field_email_checker_str = ''
    field_verified_str = ''
    field_fetching_project = []
    field_fetching_bo = []
    field_login_findUser = []
    field_login_token = []
    field_login_afterserializer = ''
    field_login_lastId = 0
    field_token_tokenresult = []
    field_token_rebase = []
    field_adminchecker_message = ''


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
                elif condition == 'fetch-project':
                    return GeneralHelper.__init__findAllProjectByEmail(params)
                elif condition == 'fetch-bo':
                    return GeneralHelper.__init__findAllBOByEmail(params)
                elif condition == 'api/check-token-identify':
                    return GeneralHelper.__init__tokenidentify(params)
                elif condition == 'api/get-users-info':
                    return GeneralHelper.__init__getcurrent_user(params)
                elif condition == 'api/check-admin-user':
                    return GeneralHelper.__init_check_admin(params)
            case 'POST':
                if condition == 'api/business-owner-registration':
                    return GeneralHelper.__init__registration_businessowner(params)
                elif condition == 'api/project-entry':
                    return GeneralHelper.__init__project_entry(params)
                elif condition == 'business-verification-dbentry':
                    return GeneralHelper.__init__verification_entry(params)
                elif condition == 'login':
                    return GeneralHelper.__init__findUsers(params)
                elif condition == 'api/gettoken':
                    return GeneralHelper.__init__checktoken(params)
            case 'PUT':
                if condition == 'api/business-update-counts':
                    return GeneralHelper.__init__update_counts(params)
                elif condition == 'api/business-update-to-verified':
                    return GeneralHelper.__init__update_to_verified(params)

    def TokenSlug(method, condition, snapshot):
        match method:
            case 'POST':
                if condition == 'tokenQueryBuild':
                    return QueryBuilder.tokenizationQueryBuild(snapshot)

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
        businessowner.sec_question = params['sec_question']
        businessowner.sec_answer = params['sec_answer']
        businessowner.save()
        GeneralParams.field_success_BO_registration = "success_bo_registration"
        return GeneralParams.field_success_BO_registration

    def __init__project_entry(params):
        project = Project()
        project.projectname = params['projectname']
        project.projectdetails = params['projectdetails']
        project.projectfeatures = params['projectfeatures']
        project.projectcategory = params['projectcategory']
        project.projectprice = params['projectprice']
        project.projectstatus = "0"
        project.projecttype = params['projecttype']
        project.clientEmail = params['email']
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

    def __init__update_to_verified(params):
        AccountVerification_1.objects.filter(
            client_email=params['email']
        ).update(verified="1")
        BusinessOwner.objects.filter(
            email=params['email']
        ).update(isverified="1")
        GeneralParams.field_verified_str = "verified_success"
        return GeneralParams.field_verified_str

    def __init__check_code_inputs(params):
        compared = AccountVerification_1.objects.filter(
            verification_code=params['code']
        ).filter(client_email=params['email']).values()
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

    def __init__findAllProjectByEmail(params):
        filtered = Project.objects.filter(
            clientEmail=params
        ).values()
        GeneralParams.field_fetching_project = filtered
        return GeneralParams.field_fetching_project

    def __init__findAllBOByEmail(params):
        filtered = BusinessOwner.objects.filter(
            email=params
        ).values()
        GeneralParams.field_fetching_bo = filtered
        return GeneralParams.field_fetching_bo

    def __init__findUsers(params):
        if params['credential_type'] == 'bo':
            bo_filtered = BusinessOwner.objects.filter(
                email=params['email']
            ).values()
            GeneralParams.field_login_findUser = bo_filtered
            return GeneralParams.field_login_findUser
        return GeneralParams.field_login_findUser

    def __init__checktoken(params):
        token_list = Tokenization.objects.filter(
            userID=params
        ).values()
        GeneralParams.field_login_token = token_list
        return GeneralParams.field_login_token

    def __init__tokenidentify(params):
        tokenize = Tokenization.objects.filter(
            userID=params
        ).values()
        GeneralParams.field_token_tokenresult = tokenize
        return GeneralParams.field_token_tokenresult

    def __init__getcurrent_user(params):
        business_account = BusinessOwner.objects.filter(
            id=params
        ).values()
        student_account = Student.objects.filter(
            id=params
        ).values()
        admin_account = Administrator.objects.filter(
            id=params
        )
        if business_account.count() > 0:
            GeneralParams.field_token_rebase = business_account
            return GeneralParams.field_token_rebase
        elif student_account.count() > 0:
            GeneralParams.field_token_rebase = student_account
            return GeneralParams.field_token_rebase
        elif admin_account.count() > 0:
            GeneralParams.field_token_rebase = admin_account
            return GeneralParams.field_token_rebase
        else:
            return GeneralParams.field_token_rebase
    
    def __init_check_admin(params):
        admincount = Administrator.objects.filter(
            userType=params
        ).values()
        if admincount.count() > 0:
            GeneralParams.field_adminchecker_message = "exist"
            return GeneralParams.field_adminchecker_message
        else:
            GeneralParams.field_adminchecker_message = "not_exist"
            return GeneralParams.field_adminchecker_message


class SystemDecryptor:
    def decrypt(webpassword, hashpassword):
        return check_password(webpassword, hashpassword)


class SystemGenerator:
    def job(size, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


class QueryBuilder:
    def tokenizationQueryBuild(snapshot):
        tokenization = Tokenization()
        tokenization.userID = snapshot['userID']
        tokenization.token = snapshot['token']
        tokenization.lastRoute = snapshot['lastRoute']
        tokenization.isDestroyed = "0"
        tokenization.isvalid = "1"
        tokenization.save()
        GeneralParams.field_login_lastId = tokenization.id
        GeneralParams.field_login_afterserializer = "success_login"
        return GeneralParams.field_login_afterserializer
