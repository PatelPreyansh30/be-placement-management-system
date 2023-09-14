from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, mixins, permissions
from . import models, serializer


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
    search_fields = ['name', 'location', 'website', 'description']
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        is_closed = self.request.query_params.get('isClosed')
        if is_closed and is_closed == "False":
            return models.CompanyModel.objects.prefetch_related('companyDocument').order_by("updatedAt").filter(isClosed=is_closed).all()
        return models.CompanyModel.objects.prefetch_related('companyDocument').order_by("updatedAt").all()
