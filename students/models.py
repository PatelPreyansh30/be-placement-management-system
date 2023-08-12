import uuid
from django.db import models

SCHOOLING_MEDIUM = (
    ('GUJ', 'Gujarati'),
    ('ENG', 'English'),
    ('HN', 'Hindi'),
)

# Create your models here.
class StudentPersonalDetailModel(models.Model):
    id = models.UUIDField(primary_key= True, default= uuid.uuid4, auto_created= True, editable= False)
    firstName = models.CharField(max_length= 50)
    lastName = models.CharField(max_length= 50)
    mobile = models.CharField(max_length= 50)
    whatsappMobile = models.CharField(max_length= 50)
    alternateMobile = models.CharField(max_length= 50)
    email = models.EmailField(max_length=100, unique=True)
    address = models.TextField()
    city = models.CharField(max_length= 50)
    isVerified = models.BooleanField(default=False)
    isBlocked = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedAt = models.DateTimeField(auto_now_add=False, auto_now=True)
    
class StudentSchoolDetailModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True, editable=False)
    studentId = models.OneToOneField(StudentPersonalDetailModel, on_delete=models.CASCADE)
    schoolingMedium = models.CharField(max_length= 50, choices= SCHOOLING_MEDIUM)
    twelvePercent = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    diplomaPercent = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    tenPercent = models.DecimalField(max_digits=4, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedAt = models.DateTimeField(auto_now_add=False, auto_now=True)

class StudentCollegeDetailModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True, editable=False)
    studentId = models.OneToOneField(StudentPersonalDetailModel, on_delete=models.CASCADE)
    enrollmentNumber = models.CharField(max_length=15, unique=True)
    college = models.CharField(max_length=15)
    branch = models.CharField(max_length=15)
    passingYear = models.IntegerField()
    currentCGPA = models.DecimalField(max_digits=3, decimal_places=2)
    currentBacklog = models.IntegerField()
    totalBacklog = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedAt = models.DateTimeField(auto_now_add=False, auto_now=True)