from rest_framework import viewsets, permissions
from . import models, serializer

# Create your views here.


class CollegeViewSet(viewsets.ModelViewSet):
    queryset = models.CollegeModel.objects.order_by('createdAt').all()
    serializer_class = serializer.CollegeSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class BranchViewSet(viewsets.ModelViewSet):
    queryset = models.BranchModel.objects.order_by('createdAt').all()
    serializer_class = serializer.BranchSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
