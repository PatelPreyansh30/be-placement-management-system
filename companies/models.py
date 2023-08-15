import uuid
from django.db import models


class CompanyModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          auto_created=True, editable=False)
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    website = models.EmailField(max_length=150)
    deadline = models.DateField()
    description = models.TextField()
    isClosed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedAt = models.DateTimeField(auto_now_add=False, auto_now=True)


class CompanyDocumentsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          auto_created=True, editable=False)
    companyId = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    document = models.FileField(upload_to='company_documents/')
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedAt = models.DateTimeField(auto_now_add=False, auto_now=True)
