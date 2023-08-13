from rest_framework import generics, viewsets
from .models import StudentModel
from .serializer import StudentSerializer

class StudentRegistrationView(generics.CreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer