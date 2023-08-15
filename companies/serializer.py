from rest_framework.serializers import ModelSerializer
from .models import CompanyModel, CompanyDocumentsModel


class CompanyDocumentSerializer(ModelSerializer):
    class Meta:
        model = CompanyDocumentsModel
        fields = '__all__'


class CompanySerializer(ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = '__all__'
