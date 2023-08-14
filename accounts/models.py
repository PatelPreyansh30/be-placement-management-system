import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import CustomUserManager


class CustomUserModel(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          auto_created=True, editable=False)
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    mobile = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    isStudent = models.BooleanField(default=False)
    isFaculty = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)
    isBlocked = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedAt = models.DateTimeField(auto_now_add=False, auto_now=True)
    username = None
    last_login = None

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
