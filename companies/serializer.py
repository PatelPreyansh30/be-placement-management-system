from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import CompanyModel, CompanyDocumentsModel


class CompanyDocumentSerializer(ModelSerializer):
    class Meta:
        model = CompanyDocumentsModel
        fields = '__all__'


class CompanySerializer(ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = '__all__'


class CompanyDocumentDetailSerializer(ModelSerializer):
    class Meta:
        model = CompanyDocumentsModel
        fields = ('id', 'document', 'updatedAt')


class CompanyDetailSerializer(ModelSerializer):
    company_document = CompanyDocumentDetailSerializer(
        many=True, read_only=True)

    class Meta:
        model = CompanyModel
        fields = ['id', 'name', 'location', 'website', 'deadline',
                  'description', 'isClosed', 'updatedAt', 'company_document']
