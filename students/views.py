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
    search_fields = ['firstName', 'lastName', 'mobile', 'email', 'studentDetail__college', 'studentDetail__enrollmentNumber', 'studentDetail__branch']
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        is_completed = self.request.query_params.get('isCompleted')
        is_verified = self.request.query_params.get('isVerified')
        is_blocked = self.request.query_params.get('isBlocked')

        if is_completed and is_completed == "True":
            return User.objects.filter(isStudent=True).prefetch_related("studentDetail").filter(studentDetail__isCompleted=True).all()
        if is_verified and is_verified == "True":
            return User.objects.filter(isStudent=True).prefetch_related("studentDetail").filter(studentDetail__isVerified=True).all()
        if is_blocked and is_blocked == "True":
            return User.objects.filter(isStudent=True).prefetch_related("studentDetail").filter(studentDetail__isBlocked=True).all()

        return User.objects.filter(isStudent=True).prefetch_related("studentDetail").all()
