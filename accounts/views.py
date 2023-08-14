from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import StudentModel
from .serializer import StudentSerializer, CustomTokenObtainPairSerializer


class StudentRegistrationView(ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
