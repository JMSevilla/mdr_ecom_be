from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ...utils.helper import GeneralHelper, GeneralParams


class TokenizationController:
    @api_view(['GET'])
    def tokenIdentify(request):
        if request.method == 'GET':
            account_userid = request.GET.get('userid')
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
                    account_userid
                )
                iterate = GeneralParams.field_token_tokenresult
                selectedField = []
                dynamicField = []
                if not bool(iterate):
                    return Response({"message": "empty_array"}, status=status.HTTP_200_OK)
                else:
                    for field in iterate:
                        selectedField = [
                            field['isvalid'],
                            field['lastRoute']
                        ]
                    if selectedField[0] == '1':
                        if selectedField[1] == 'business_platform':
                            GeneralHelper.Slug(
                                'GET',
                                'api/get-users-info',
                                account_userid
                            )
                            for dynamicFieldSelected in GeneralParams.field_token_rebase:
                                dynamicField = [
                                    dynamicFieldSelected['firstname'],
                                    dynamicFieldSelected['lastname'],
                                    dynamicFieldSelected['email'],
                                    dynamicFieldSelected['imgURL'],
                                    dynamicFieldSelected['id'],
                                    selectedField[1],
                                    'token_exist_business_platform'
                                ]
                            return Response({
                                "message": dynamicField
                            }, status=status.HTTP_200_OK)
                return Response({
                    "data": GeneralParams.field_token_tokenresult
                }, status=status.HTTP_200_OK)
