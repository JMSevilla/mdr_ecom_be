from rest_framework import status
from rest_framework.response import Response
from restful_api.utils.Configuration.emailconfig import EmailConfig, EmailConfigResponse
from rest_framework.decorators import api_view

from restful_api.utils.student_helper import StudentHelper, StudentParams


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
