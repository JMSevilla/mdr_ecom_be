from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from restful_api.models import ProductCategories

class ProductsController:
    @api_view(['POST'])
    def addProjectCategories(request):
        if request.method == 'POST':
            categoryName = request.POST.get('categoryName')
            projectentity = ProductCategories()
            projectentity.categoryName = categoryName
            projectentity.isActive = "1"
            projectentity.save()
            return Response({"message" : "success_product_category"}, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def getAllProjectCategories(request):
        if request.method == 'GET':
            filteredAll = ProductCategories.objects.all().values()
            return Response(filteredAll, status=status.HTTP_200_OK)

    @api_view(['DELETE'])
    def removeProjectCategories(request, id):
        if request.method == 'DELETE':
            ProductCategories.objects.filter(id=id).delete()
            return Response({"message" : "success_delete"}, status=status.HTTP_200_OK)