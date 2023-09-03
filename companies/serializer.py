from rest_framework import serializers
from .models import CompanyModel, CompanyDocumentsModel


class CompanyDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDocumentsModel
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = '__all__'


class CompanyDocumentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDocumentsModel
        fields = ('id', 'document', 'updatedAt')


class CompanyDetailSerializer(serializers.ModelSerializer):
    companyDocument = CompanyDocumentDetailSerializer(
        many=True, read_only=True)

    class Meta:
        model = CompanyModel
        fields = ['id', 'name', 'location', 'website', 'deadline',
                  'description', 'isClosed', 'updatedAt', 'companyDocument']
