from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import StudentPersonalDetailModel, StudentCollegeDetailModel, StudentSchoolDetailModel
from .serializer import StudentPersonalDetailSerializer, StudentCollegeDetailSerializer, StudentSchoolDetailSerializer


class StudentPersonalDetailView(ModelViewSet):
    queryset = StudentPersonalDetailModel.objects.all()
    serializer_class = StudentPersonalDetailSerializer
    # permission_classes = [IsAuthenticated]


class StudentCollegeDetailView(ModelViewSet):
    queryset = StudentCollegeDetailModel.objects.all()
    serializer_class = StudentCollegeDetailSerializer
    # permission_classes = [IsAuthenticated]


class StudentSchoolDetailView(ModelViewSet):
    queryset = StudentSchoolDetailModel.objects.all()
    serializer_class = StudentSchoolDetailSerializer
    # permission_classes = [IsAuthenticated]
