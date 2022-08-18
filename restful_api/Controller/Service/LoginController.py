from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ...utils.helper import GeneralHelper, GeneralParams, SystemDecryptor, SystemGenerator


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        if request.POST.get('ct') == 'bo':
            pass_data = {
                "email": request.POST.get('email'),
                "password": request.POST.get('password'),
                "credential_type": request.POST.get('ct')
            }
            GeneralHelper.Slug(
                'POST',
                'login',
                pass_data
            )
            res = GeneralParams.field_login_findUser
            nodehelper = []
            tokerow = []
            if res:
                for node in res:
                    nodehelper = [
                        node['password'],
                        node['userType'],
                        node['isLock'],
                        node['id'],
                        node['firstname'],
                        node['lastname'],
                        node['email']
                    ]
                getdecrypt = SystemDecryptor.decrypt(
                    pass_data['password'], nodehelper[0])
                if getdecrypt:
                    if nodehelper[2] == '1':
                        return Response({"message": "ACCOUNT_LOCK"}, status=status.HTTP_200_OK)
                    else:
                        if nodehelper[1] == '3':
                            GeneralHelper.Slug(
                                'POST', 'api/gettoken', nodehelper[3])
                            if GeneralParams.field_login_token.count() != 0:
                                for tokenode in GeneralParams.field_login_token:
                                    tokerow = [
                                        tokenode['isvalid']
                                    ]
                                if tokerow[0] == '1':
                                    return Response({"message": "invalid"}, status=status.HTTP_200_OK)
                                else:
                                    collection = {
                                        "userID": nodehelper[3],
                                        "lastRoute": "business_platform",
                                        "token": SystemGenerator.job(50)
                                    }
                                    GeneralHelper.TokenSlug(
                                        'POST',
                                        'tokenQueryBuild',
                                        collection
                                    )
                                    responseCollection = [
                                        nodehelper[4],
                                        nodehelper[5],
                                        nodehelper[6],
                                        'success_business_platform',
                                        'business_owner',
                                        nodehelper[3],
                                        GeneralParams.field_login_lastId
                                    ]
                                    return Response({"message": GeneralParams.field_login_afterserializer,
                                                     'response_data': responseCollection}, status=status.HTTP_200_OK)
                            else:
                                collection = {
                                    "userID": nodehelper[3],
                                    "lastRoute": "business_platform",
                                    "token": SystemGenerator.job(50)
                                }
                                GeneralHelper.TokenSlug(
                                    'POST',
                                    'tokenQueryBuild',
                                    collection
                                )
                                responseCollection = [
                                    nodehelper[4],
                                    nodehelper[5],
                                    nodehelper[6],
                                    'success_business_platform',
                                    'business_owner',
                                    nodehelper[3],
                                    GeneralParams.field_login_lastId
                                ]
                                return Response({"message": GeneralParams.field_login_afterserializer,
                                                 'response_data': responseCollection}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "PASSWORD_INVALID"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "ACCOUNT_NOT_FOUND"}, status=status.HTTP_200_OK)
        elif request.POST.get('ct') == 'student':
            return
        elif request.POST.get('ct') == 'admin':
            return
