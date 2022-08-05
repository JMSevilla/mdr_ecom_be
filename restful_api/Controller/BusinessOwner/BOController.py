from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework import status
from restful_api.utils.helper import GeneralParams
from restful_api.utils.helper import GeneralHelper
from rest_framework.decorators import api_view



@api_view(['GET'])
def checkemail(request, email):
    if request.method == 'GET':
        GeneralHelper.Slug(
            'GET',
            'api/checking-email',
            email
        )
    return Response({"message" : GeneralParams.params_result}, status=status.HTTP_200_OK)

@api_view(['POST'])
def businessowner_registration(request):
    if request.method == 'POST':
        collection = {
            "firstname":request.POST.get('firstname'),
            "lastname":request.POST.get('lastname'),
            "contactnumber":request.POST.get('contactnumber'),
            "address":request.POST.get('address'),
            "email":request.POST.get('email'),
            "password":request.POST.get('password'),
            "isverified": request.POST.get('isverified')
        }
        GeneralHelper.Slug(
            'POST',
            'api/business-owner-registration',
            collection
        )
        if GeneralParams.field_success_BO_registration == "success_bo_registration":
            return Response({"message":GeneralParams.field_success_BO_registration}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"something_wrong"}, status=status.HTTP_400_BAD_REQUEST)