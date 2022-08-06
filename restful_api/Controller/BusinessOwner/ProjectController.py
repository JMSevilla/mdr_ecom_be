from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework import status
from restful_api.utils.helper import GeneralParams
from restful_api.utils.helper import GeneralHelper
from rest_framework.decorators import api_view


class ProjectController:
    @api_view(['POST'])
    def projectEntry(request):
        if request.method == 'POST':
            if request.POST.get('projectname') is None:
                return Response({"message":"empty"}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"message":"not_empty"}, status=status.HTTP_200_OK)