import uuid
from django.db import models
from companies.models import CompanyModel
from students.models import StudentModel


class PlacementApplicationModel(models.Model):

    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interviewed', 'Interviewed'),
        ('placed', 'Placed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          auto_created=True, editable=False)
    studentId = models.ForeignKey(
        StudentModel, on_delete=models.CASCADE, related_name="appliedStudent")
    companyId = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, related_name="appliedCompany")
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=20, default='applied')
    appliedAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedAt = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return str(self.id)

