from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from restful_api.utils.helper import GeneralParams
from restful_api.utils.helper import GeneralHelper
from restful_api.models import TrainingManagement_1

class TrainingController:
    @api_view(['POST'])
    def addTraining(request):
        if request.method == 'POST':
            collective = {
                "title": request.POST.get('title'),
                "category" : request.POST.get('category'),
                "description" : request.POST.get('description'),
                "days" : request.POST.get('days'),
                "imgurl" : request.POST.get('imgurl'),
                "status" : request.POST.get('status'),
                "level" : request.POST.get('level'),
                "proctor" : request.POST.get('proctor'),
                "capacity" : request.POST.get('capacity')
            }
            GeneralHelper.Slug(
                'POST',
                'api/training-add',
                collective
            )
            return Response({"message" : GeneralParams.field_save_admin_training_message}, status=status.HTTP_200_OK)
        return Response({"message": "invalid_request"}, status=status.HTTP_200_OK)
    
    @api_view(['GET'])
    def getAllTrainings(request):
        if request.method == 'GET':
            GeneralHelper.Slug(
                'GET',
                'api/get-alltrainings',
                None
            )
            return Response(GeneralParams.field_get_alltrainings, status=status.HTTP_200_OK)

    @api_view(['POST'])
    def editTrainings(request):
        if request.method == 'POST':
            collection = {
                "id" : request.POST.get('id'),
                "title" : request.POST.get('title'),
                "category" : request.POST.get('category'),
                "days" : request.POST.get('days'),
                "status" : request.POST.get('status'),
                "level" : request.POST.get('level')
            }
            TrainingManagement_1.objects.filter(
                id=collection['id']
            ).update(
                trainingTitle=collection['title'],
                trainingCategory=collection['category'],
                trainingDays=collection['days'],
                trainingStatus=collection['status'],
                trainingLevel=collection['level']
            )
            return Response("success_edit_training", status=status.HTTP_200_OK)

    @api_view(['DELETE'])
    def removeTraining(request, id):
        if request.method == 'DELETE':
            TrainingManagement_1.objects.filter(id=id).delete()
            return Response("delete_success", status=status.HTTP_200_OK)