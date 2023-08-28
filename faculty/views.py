from rest_framework import viewsets, permissions, mixins
from django.contrib.auth import get_user_model
from . import models, serializer

User = get_user_model()


class FacultyView(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = models.FacultyModel.objects.all()
    serializer_class = serializer.FacultySerializer
    # permission_classes = [permissions.IsAuthenticated]


class FacultyDetailedView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = serializer.FacultyDetailedSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(isStaff=True).prefetch_related('facultyDetail').all()
