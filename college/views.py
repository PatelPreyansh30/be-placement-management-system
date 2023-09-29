from rest_framework import viewsets, permissions
from . import models, serializer

# Create your views here.


class CollegeViewSet(viewsets.ModelViewSet):
    queryset = models.CollegeModel.objects.all()
    serializer_class = serializer.CollegeSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
