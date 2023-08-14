from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import StudentPersonalDetailModel
from .serializer import StudentPersonalDetailSerializer


class StudentPersonalDetailView(ModelViewSet):
    queryset = StudentPersonalDetailModel.objects.all()
    serializer_class = StudentPersonalDetailSerializer
