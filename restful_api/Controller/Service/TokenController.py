from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from restful_api.models import Tokenization

from ...utils.helper import GeneralHelper, GeneralParams
from django.contrib.auth.hashers import check_password
from ...utils.encrypt_util import MDRHasher


class TokenizationController:
    @api_view(['POST'])
    def tokenIdentify(request):
        if request.method == 'POST':
            account_userid = MDRHasher.decrypt(request.POST.get('userid'))
            authtoke = MDRHasher.decrypt(request.POST.get('token'))
            collection = {
                "uid" : account_userid,
                "auth" : authtoke
            }
            if account_userid == 'unknown':
                return Response({
                    "message": "invalid_token"
                }, status=status.HTTP_200_OK)
            elif account_userid == 'unknown1':
                return Response({
                    "message": "invalid_token"
                }, status=status.HTTP_200_OK)
            else:
                GeneralHelper.Slug(
                    'GET',
                    'api/check-token-identify',
                    collection
                )
                iterate = GeneralParams.field_token_tokenresult
                selectedField = []
                dynamicField = []
                if not bool(iterate):
                    return Response({"message": "not_exist"}, status=status.HTTP_200_OK)
                else:
                    for field in iterate:
                        selectedField = [
                            field['isvalid'],
                            field['lastRoute']
                        ]
                    if selectedField[0] == '1':
                        if selectedField[1] == 'business_platform':
                            return Response({
                                "data": GeneralParams.field_token_tokenresult
                            }, status=status.HTTP_200_OK)
                        elif selectedField[1] == 'admin_platform':
                            return Response({
                                "data": GeneralParams.field_token_tokenresult
                            }, status=status.HTTP_200_OK)
                    else:
                        return Response({
                            "data": "invalid_token"
                        }, status=status.HTTP_200_OK)
        return Response({
                        "data": "invalid_request"
                        }, status=status.HTTP_200_OK)


@api_view(['POST'])
def route_token_checker(request):
    if request.method == 'POST':
        collection = {
                "key" : MDRHasher.decrypt(request.POST.get('key')),
                "authtoken" : MDRHasher.decrypt(request.POST.get('token'))
            }
        prlog = Tokenization.objects.filter(
            userID=collection['key'], token=collection['authtoken'],
            isvalid='1'
        ).values()
        if prlog.count() > 0:
            return Response({
                "message" : "protected"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "message" : "unprotected"
            }, status=status.HTTP_200_OK)