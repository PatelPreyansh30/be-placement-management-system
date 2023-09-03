from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, mixins, permissions
from . import models, serializer, pagination


class CompanyView(mixins.CreateModelMixin,
                  mixins.DestroyModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = models.CompanyModel.objects.all()
    serializer_class = serializer.CompanySerializer
    # permission_classes = [permissions.IsAuthenticated]


class CompanyDocumentView(mixins.CreateModelMixin,
                          mixins.DestroyModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = models.CompanyDocumentsModel.objects.all()
    serializer_class = serializer.CompanyDocumentSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CompanyDetailView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializer.CompanyDetailSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]
    # filterset_fields = ['id']
    search_fields = ['name', 'location', 'website', 'description']
    pagination_class = pagination.CustomCompanyPagination
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.CompanyModel.objects.prefetch_related('companyDocument').order_by("updatedAt").all()
