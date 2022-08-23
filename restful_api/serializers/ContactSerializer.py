from rest_framework import serializers
from restful_api.models import ContactUs

class ContactUsSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = ContactUs
        fields = (
            'id',
            'fullname',
            'email',
            'subject',
            'message'
        )
    
    def create(self, validated_data):
        fullname = validated_data.get('fullname')
        email = validated_data.get('email')
        subject = validated_data.get('subject')
        message = validated_data.get('message')
        contactus = ContactUs.objects.create(
            fullname=fullname,
            email=email,
            subject=subject,
            message=message
        )
        return contactus