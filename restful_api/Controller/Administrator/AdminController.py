from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from restful_api.utils.helper import GeneralParams
from restful_api.utils.helper import GeneralHelper


class AdministratorController:
    @api_view(['GET'])
    def check_admin_controller(request):
        if request.method == 'GET':
            GeneralHelper.Slug(
                'GET',
                'api/check-admin-user',
                '1'
            )
            return Response({"message": GeneralParams.field_adminchecker_message}, status=status.HTTP_200_OK)
        return Response({"message": "invalid_request"}, status=status.HTTP_100_CONTINUE)

    @api_view(['POST'])
    def admin_registration_controller(request):
        if request.method == 'POST':
            get_params = {
                "firstname": request.POST.get('firstname'),
                "lastname": request.POST.get('lastname'),
                "email": request.POST.get('email'),
                "password": request.POST.get('password')
            }
            GeneralHelper.Slug(
                'POST',
                'admin/registration',
                get_params
            )
            return Response({"message": GeneralParams.field_save_adminreg_message}, status=status.HTTP_200_OK)
        return Response({"message": "invalid_request"}, status=status.HTTP_200_OK)
