import string
import random
from restful_api.models import Student, AccountVerification_1
from django.contrib.auth.hashers import make_password
from django.db.models import F


class StudentParams:
    field_check_counts = ''
    field_update_counts = ''


class StudentHelper:
    def Snapshot(method, condition, params):
        match method:
            case 'GET':
                if condition == 'api/check-sentcount-before-update':
                    return StudentHelper.__initialize__verifycheck_counts(params)
            case 'POST':
                return
            case 'PUT':
                if condition == 'api/business-update-counts':
                    return StudentHelper.__initialize__updateCounts(params)

    def __initialize__verifycheck_counts(params):
        scan_counts = AccountVerification_1.objects.filter(
            client_email=params
        ).filter(sent_count__gte=3).values()
        if scan_counts.count() > 0:
            StudentParams.field_check_counts = "exceed_email"
            return StudentParams.field_check_counts
        StudentParams.field_check_counts = "success"
        return StudentParams.field_check_counts

    def __initialize__updateCounts(params):
        AccountVerification_1.objects.filter(
            client_email=params['email']
        ).update(sent_count=F('sent_count')+1, verification_code=params['code'])
        StudentParams.field_update_counts = "success"
        return StudentParams.field_update_counts
