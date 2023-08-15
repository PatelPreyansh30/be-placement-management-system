from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import StudentPersonalDetailModel, StudentCollegeDetailModel
from .serializer import StudentPersonalDetailSerializer, StudentCollegeDetailSerializer


class StudentPersonalDetailView(ModelViewSet):
    queryset = StudentPersonalDetailModel.objects.all()
    serializer_class = StudentPersonalDetailSerializer
    permission_classes = [IsAuthenticated]


class StudentCollegeDetailView(ModelViewSet):
    queryset = StudentCollegeDetailModel.objects.all()
    serializer_class = StudentCollegeDetailSerializer
    permission_classes = [IsAuthenticated]
