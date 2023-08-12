import uuid
from django.db import models

# Create your models here.
class StudentProfileModel(models.Model):
    id = models.UUIDField(primary_key= True, default= uuid.uuid4, auto_created= True, editable= False)
    firstName = models.CharField(max_length= 50)
    lastName = models.CharField(max_length= 50)
    mobile = models.CharField(max_length= 50)
    whatsappMobile = models.CharField(max_length= 50)
    alternateMobile = models.CharField(max_length= 50)
    address = models.TextField()
    city = models.CharField(max_length= 50)
    
class StudentEducationModel(models.Model):
    SCHOOLING_MEDIUM = (
        ('GUJ', 'Gujarati'),
        ('ENG', 'English'),
        ('HN', 'Hindi'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True, editable=False)
    studentId = models.ForeignKey(StudentProfileModel, on_delete=models.CASCADE)
    
    schoolingMedium = models.CharField(max_length= 50, choices= SCHOOLING_MEDIUM)