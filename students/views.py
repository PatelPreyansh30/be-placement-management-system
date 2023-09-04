from rest_framework import mixins, viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from . import serializer, models

User = get_user_model()


class StudentCreateView(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = models.StudentModel.objects.all()
    serializer_class = serializer.StudentSerializer
    # permission_classes = [permissions.IsAuthenticated]


class StudentDetailedView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = serializer.StudentDetailedSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['firstName', 'lastName', 'mobile', 'email']
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(isStudent=True).prefetch_related("studentDetail").all()
