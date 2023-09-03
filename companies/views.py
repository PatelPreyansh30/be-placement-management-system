from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import CustomCompanyPagination
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
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = ['id']
    search_fields = ['name', 'location', 'website', 'description']
    ordering_fields = ['updatedAt']
    pagination_class = CustomCompanyPagination
    # permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return CompanyModel.objects.prefetch_related('company_document').all()



class ClosedCompanyView(ReadOnlyModelViewSet):
    queryset = CompanyModel.objects.filter(isClosed=True).all()
    serializer_class = CompanySerializer
    # permission_classes = [IsAuthenticated]


class OpenCompanyView(ReadOnlyModelViewSet):
    queryset = CompanyModel.objects.filter(isClosed=False).all()
    serializer_class = CompanySerializer
    # permission_classes = [IsAuthenticated]
