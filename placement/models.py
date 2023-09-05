import uuid
from django.db import models
from companies.models import CompanyModel
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class PlacementApplicationModel(models.Model):

    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interviewed', 'Interviewed'),
        ('placed', 'Placed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,auto_created=True,editable=False)
    studentId = models.OneToOneField(
        UserModel, on_delete=models.CASCADE, related_name="studentApplicationDetail")
    companyId = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='applied')
    appliedAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedAt = models.DateTimeField(auto_now_add=False, auto_now=True)
