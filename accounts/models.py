import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import StudentManager

class StudentModel(AbstractBaseUser):
    id = models.UUIDField(primary_key= True, default= uuid.uuid4, auto_created= True, editable= False)
    username = None
    firstName = models.CharField(max_length= 150)
    lastName = models.CharField(max_length= 150)
    mobile = models.CharField(max_length= 150, unique=True)
    whatsappMobile = models.CharField(max_length= 150)
    alternateMobile = models.CharField(max_length= 150)
    email = models.EmailField(max_length=150, unique=True)
    address = models.TextField()
    city = models.CharField(max_length= 150)
    isVerified = models.BooleanField(default=False)
    isBlocked = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedAt = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    objects = StudentManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []