import smtplib
from rest_framework import status
from rest_framework.response import Response
from restful_api.utils.Configuration.emailconfig import EmailConfig, EmailConfigResponse
from rest_framework.decorators import api_view

from restful_api.utils.student_helper import StudentHelper, StudentParams
from django.conf import settings

class StudentController:
    @api_view(['GET'])
    def studentCheckEmail(request, email):
        if request.method == 'GET':
            EmailConfig.student_config_checkemail(
                email
            )
            return Response({
                "message": EmailConfigResponse.student_email_message
            }, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def student_verify_email(request, email):
        if request.method == 'GET':
            StudentHelper.Snapshot(
                'GET',
                'api/check-email-before-push',
                email
            )
            return Response({"message" : StudentParams.field_email_checker_str}, status=status.HTTP_200_OK)

    @api_view(['POST'])
    def student_verification_record(request):
        if request.method == 'POST':
            collection = {
                "email" : request.POST.get('email'),
                "code" : request.POST.get('code')
            }
            StudentHelper.Snapshot(
                'POST',
                'api/student-verification-entry',
                collection
            )
            return Response({"message" : StudentParams.field_verification_student }, status=status.HTTP_200_OK)

    @api_view(['POST'])
    def student_verification(request, email, code):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(settings.EMAIL_HOST_USER, settings.PY_EMAIL_PASS)
        subject = 'MDR Ecommerce Verification Code'
        text = code
        message = 'Subject: {}\n\n{}'.format(subject, text)
        s.sendmail(settings.EMAIL_HOST_USER,
                email, message)
        s.quit()
        return Response(
            {
                "message": "success_sent"
            },
            status=status.HTTP_200_OK
        )

    @api_view(['GET', 'PUT'])
    def student_update_with_sendemail(request, email, code):
        if request.method == 'PUT':
            EmailConfig.sendEmailHelper(email, code)
            collection = { 
                "email" : email,
                "code" : code
            }
            StudentHelper.Snapshot(
                'PUT',
                'api/student-update-counts',
                collection
            )
            return Response({"message" : StudentParams.field_update_sent_count_message}, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def student_verification_checkcounts(request, email, code):
        if request.method == 'GET':
            StudentHelper.Snapshot(
                'GET',
                'api/check-sentcount-before-update',
                email
            )
            if StudentParams.field_check_counts == 'exceed_email':
                return Response({
                    "message": StudentParams.field_check_counts
                }, status=status.HTTP_200_OK)
            else:
                EmailConfig.sendEmailHelper(
                    email, code
                )
                collection = {
                    "email": email,
                    "code": code
                }
                StudentHelper.Snapshot(
                    'PUT',
                    'api/business-update-counts',
                    collection
                )
                return Response({"message": StudentParams.field_update_counts}, status=status.HTTP_200_OK)
        return Response({"message": StudentParams.field_update_counts}, status=status.HTTP_200_OK)
