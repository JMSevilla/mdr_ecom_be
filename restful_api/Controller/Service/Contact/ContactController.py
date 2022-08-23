import re
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from restful_api.serializers.ContactSerializer import ContactUsSerilizer

class ContactController:
    @api_view(['POST'])
    def sendMessage(request):
        if request.method == 'POST':
            contactus_serializer = ContactUsSerilizer(data=request.data)
            if contactus_serializer.is_valid():
                contactus_serializer.save()
                return Response({"message" : "success_sent_message"}, status=status.HTTP_200_OK)
            return Response({"error_message": contactus_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)