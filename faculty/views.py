from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from . import models, serializer

User = get_user_model()


class FacultyPersonalView(viewsets.ModelViewSet):
    queryset = models.FacultyPersonalModel.objects.all()
    serializer_class = serializer.FacultyPersonalSerializer
    # permission_classes = [permissions.IsAuthenticated]


class FacultyDashboardView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializer.FacultyDashboardSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(isStaff=True).prefetch_related('accountDetail').all()
