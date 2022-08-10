from rest_framework import serializers
from restful_api.models import Project


class ProjectSerializer(serializers.ModelSerializer) :
    
    class Meta:
        model = Project
        fields = (
            'id',
            'projectname',
            'projectdetails',
            'projectcategory',
            'projecttype',
            'projectfeatures',
            'projectprice',
            'clientEmail',
            'projectstatus',
            'created_at',
            'updated_at'
        )