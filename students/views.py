from rest_framework import mixins, viewsets, permissions
from django.contrib.auth import get_user_model
from . import serializer, models

User = get_user_model()


class StudentPersonalDetailView(viewsets.ModelViewSet):
    queryset = models.StudentPersonalDetailModel.objects.all()
    serializer_class = serializer.StudentPersonalDetailSerializer
    # permission_classes = [IsAuthenticated]


class StudentCollegeDetailView(viewsets.ModelViewSet):
    queryset = models.StudentCollegeDetailModel.objects.all()
    serializer_class = serializer.StudentCollegeDetailSerializer
    # permission_classes = [IsAuthenticated]


class StudentSchoolDetailView(viewsets.ModelViewSet):
    queryset = models.StudentSchoolDetailModel.objects.all()
    serializer_class = serializer.StudentSchoolDetailSerializer
    # permission_classes = [IsAuthenticated]


class StudentDetailedViewset(viewsets.ModelViewSet):
    serializer_class = serializer.StudentDetailedSerializer

    def get_queryset(self):
        return models.StudentPersonalDetailModel.objects.select_related('studentId').prefetch_related('college_detail').prefetch_related('college_detail').all()


class StudentForDashboardView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializer.StudentForDashboardSerializer

    def get_queryset(self):
        return User.objects.filter(isStudent=True).prefetch_related("accountDetail").all()
