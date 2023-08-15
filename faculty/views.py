from rest_framework.viewsets import ModelViewSet
from .models import FacultyPersonalModel
from .serializer import FacultyPersonalSerializer


class FacultyPersonalView(ModelViewSet):
    queryset = FacultyPersonalModel.objects.all()
    serializer_class = FacultyPersonalSerializer
