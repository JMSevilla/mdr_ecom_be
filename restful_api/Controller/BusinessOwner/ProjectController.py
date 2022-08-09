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
                return Response({"message": "empty"}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"message": "not_empty"}, status=status.HTTP_200_OK)

    @api_view(['POST'])
    def create_project(request):
        if request.method == 'POST':
            collection = {
                "projectname" : request.POST.get('projectname'),
                "projectdetails" : request.POST.get('projectdetails'),
                "projectfeatures" : request.POST.get('projectfeatures'),
                "projectcategory" : request.POST.get('projectcategory'),
                "projectprice" : request.POST.get('projectprice'),
                "projecttype" : request.POST.get('projecttype'),
                "email" : request.POST.get('email')
            }
            GeneralHelper.Slug(
                'POST',
                'api/project-entry',
                collection
            )
            if GeneralParams.field_success_Project_entry == "success_bo_registration":
                return Response({"message": GeneralParams.field_success_Project_entry}, status=status.HTTP_200_OK)
            else:
                return Response({
                    "message": GeneralParams.field_success_Project_entry
                }, status=status.HTTP_200_OK)
        return Response({
            "message": collection
        }, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def __fetch_project__(request, email):
        GeneralHelper.Slug(
            'GET',
            'fetch-project',
            email
        )
        return Response({"data" : GeneralParams.field_fetching_project},
        status=status.HTTP_200_OK)
