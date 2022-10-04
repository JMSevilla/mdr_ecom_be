import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...utils.helper import GeneralHelper, GeneralParams
from restful_api.models import Tokenization


class SignoutController:
    @api_view(['POST'])
    def signout(request):
        if request.method == 'POST':
            collection = {
                "id" : request.POST.get("userID"),
                "token" : request.POST.get("token")
            }
            signout_account = Tokenization.objects.filter(
            userID=collection["id"]
            ).values()
            token_identifier = Tokenization.objects.filter(
                token=collection["token"]
            ).values()
            if signout_account.count() > 0:
                if token_identifier.count() > 0:
                    Tokenization.objects.filter(
                        userID=collection["id"]
                    ).update(
                        isDestroyed="1", isvalid="0"
                    )
                    return Response({"message" : "signout_success"}, status=status.HTTP_200_OK)
                else:
                    return Response({"message" : "token_not_match"}, status=status.HTTP_200_OK)
            else:
                return Response({"message" : "no_account_found"}, status=status.HTTP_100_CONTINUE)

