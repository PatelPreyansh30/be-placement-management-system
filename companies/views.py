from rest_framework.viewsets import ModelViewSet
from .models import CompanyModel, CompanyDocumentsModel
from .serializer import CompanySerializer, CompanyDocumentSerializer


class CompanyView(ModelViewSet):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer
