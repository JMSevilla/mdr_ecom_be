from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password

from ...utils.helper import GeneralHelper, GeneralParams, SystemDecryptor, SystemGenerator
from ...utils.encrypt_util import MDRHasher


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        pass_data = {
            "email": request.POST.get('email'),
            "password": request.POST.get('password')
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
                            if tokerow[0] == '0':
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
                                    MDRHasher.encrypt(nodehelper[3]),
                                    GeneralParams.field_login_lastId,
                                    MDRHasher.encrypt(collection['token'])
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
                                    MDRHasher.encrypt(nodehelper[3]),
                                    GeneralParams.field_login_lastId,
                                    MDRHasher.encrypt(collection['token'])
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
                                MDRHasher.encrypt(nodehelper[3]),
                                GeneralParams.field_login_lastId,
                                MDRHasher.encrypt(collection['token'])
                            ]
                            return Response({"message": GeneralParams.field_login_afterserializer,
                                             'response_data': responseCollection}, status=status.HTTP_200_OK)
                    elif nodehelper[1] == '1':
                        GeneralHelper.Slug(
                            'POST', 'api/gettoken', nodehelper[3])
                        if GeneralParams.field_login_token.count() != 0:
                            for tokenode in GeneralParams.field_login_token:
                                tokerow = [
                                    tokenode['isvalid']
                                ]
                            if tokerow[0] == '0':
                                collection = {
                                    "userID": nodehelper[3],
                                    "lastRoute": "admin_platform",
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
                                    'success_admin_platform',
                                    'admin_dev',
                                    MDRHasher.encrypt(nodehelper[3]),
                                    GeneralParams.field_login_lastId,
                                    MDRHasher.encrypt(collection['token'])
                                ]
                                return Response({"message": GeneralParams.field_login_afterserializer,
                                                 'response_data': responseCollection}, status=status.HTTP_200_OK)
                            else:
                                collection = {
                                    "userID": nodehelper[3],
                                    "lastRoute": "admin_platform",
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
                                    'success_admin_platform',
                                    'admin_dev',
                                    MDRHasher.encrypt(nodehelper[3]),
                                    GeneralParams.field_login_lastId,
                                    MDRHasher.encrypt(collection['token'])
                                ]
                                return Response({"message": GeneralParams.field_login_afterserializer,
                                                 'response_data': responseCollection}, status=status.HTTP_200_OK)
                        else:
                            collection = {
                                "userID": nodehelper[3],
                                "lastRoute": "admin_platform",
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
                                'success_admin_platform',
                                'admin_dev',
                                MDRHasher.encrypt(nodehelper[3]),
                                GeneralParams.field_login_lastId,
                                MDRHasher.encrypt(collection['token'])
                            ]
                            return Response({"message": GeneralParams.field_login_afterserializer,
                                             'response_data': responseCollection}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "PASSWORD_INVALID"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "ACCOUNT_NOT_FOUND"}, status=status.HTTP_200_OK)
