import string
import random
from restful_api.models import Student, AccountVerification_1
from django.contrib.auth.hashers import make_password
from django.db.models import F


class StudentParams:
    field_check_counts = ''
    field_update_counts = ''
    field_email_checker_str = ''
    field_verification_student = ''
    field_update_sent_count_message = ''

class StudentHelper:
    def Snapshot(method, condition, params):
        match method:
            case 'GET':
                if condition == 'api/check-sentcount-before-update':
                    return StudentHelper.__initialize__verifycheck_counts(params)
                elif condition == 'api/check-email-before-push':
                    return StudentHelper.__initialize_checkemail_before_push(params)
            case 'POST':
                if condition == 'api/student-verification-entry':
                    return StudentHelper.__initialize_verification_entry(params)
            case 'PUT':
                if condition == 'api/student-update-counts':
                    return StudentHelper.__initialize_update_counts_student(params)

    def __initialize_checkemail_before_push(params):
        filtered = AccountVerification_1.objects.filter(
            client_email=params
        ).values()
        if filtered.count() > 0:
            onCount = AccountVerification_1.objects.filter(
                sent_count=3
            ).values()
            if onCount.count() > 0:
                StudentParams.field_email_checker_str = 'exceed_limit'
            else:
                StudentParams.field_email_checker_str = 'update_another_sent_count'
        else:
            StudentParams.field_email_checker_str = 'does_not_exist'
            return StudentParams.field_email_checker_str

    def __initialize_verification_entry(params):
        account_verification = AccountVerification_1()
        account_verification.client_email = params['email']
        account_verification.verification_code = params['code']
        account_verification.verified = '0'
        account_verification.user_type = '2'
        account_verification.sent_count = 1
        account_verification.save()
        StudentParams.field_verification_student = 'success_vc_entry'
        return StudentParams.field_verification_student

    def __initialize__verifycheck_counts(params):
        scan_counts = AccountVerification_1.objects.filter(
            client_email=params
        ).filter(sent_count__gte=3).values()
        if scan_counts.count() > 0:
            StudentParams.field_check_counts = "exceed_email"
            return StudentParams.field_check_counts
        StudentParams.field_check_counts = "success"
        return StudentParams.field_check_counts


    def __initialize_update_counts_student(params):
        AccountVerification_1.objects.filter(
            client_email=params['email']
        ).update(sent_count=F('sent_count')+1, verification_code=params['code'])
        StudentParams.field_update_sent_count_message = "success"
        return StudentParams.field_update_sent_count_message