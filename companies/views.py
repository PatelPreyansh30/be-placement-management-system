from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import CompanyModel, CompanyDocumentsModel
from .serializer import CompanySerializer, CompanyDocumentSerializer, CompanyDetailSerializer


class CompanyView(ModelViewSet):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer
    # permission_classes = [IsAuthenticated]


class CompanyDocumentView(ModelViewSet):
    queryset = CompanyDocumentsModel.objects.all()
    serializer_class = CompanyDocumentSerializer
    # permission_classes = [IsAuthenticated]


class CompanyDetailView(ReadOnlyModelViewSet):
    serializer_class = CompanyDetailSerializer

    def get_queryset(self):
        return CompanyModel.objects.prefetch_related('company_document').all()

    # permission_classes = [IsAuthenticated]


class ClosedCompanyView(ReadOnlyModelViewSet):
    queryset = CompanyModel.objects.filter(isClosed=True).all()
    serializer_class = CompanySerializer
    # permission_classes = [IsAuthenticated]


class OpenCompanyView(ReadOnlyModelViewSet):
    queryset = CompanyModel.objects.filter(isClosed=False).all()
    serializer_class = CompanySerializer
    # permission_classes = [IsAuthenticated]
