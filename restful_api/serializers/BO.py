from rest_framework import serializers
from restful_api.models import BusinessOwner


class BusinessOwnerSerializer(serializers.ModelSerializer) :
    
    class Meta:
        model = BusinessOwner
        fields = (
            'id',
            'firstname',
            'lastname',
            'contactnumber',
            'address',
            'email',
            'password',
            'userType',
            'isLock',
            'isverified',
            'imgURL',
            'created_at',
            'updated_at'
        )