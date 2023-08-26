import uuid
from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

SCHOOLING_MEDIUM = (
    ('GUJ', 'Gujarati'),
    ('ENG', 'English'),
    ('HN', 'Hindi'),
)


class StudentPersonalDetailModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          auto_created=True, editable=False)
    studentId = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="accountDetail")
    whatsappMobile = models.CharField(max_length=150)
    alternateMobile = models.CharField(max_length=150)
    address = models.TextField()
    profilePic = models.ImageField(upload_to="student_profile_pic/")
    resume = models.FileField(upload_to="student_resume/")
    placementGuidelineForm = models.FileField(
        upload_to="student_placement_guidelines_form/")
    isCompleted = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)
    isBlocked = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedAt = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.id

    def delete(self, *args, **kwargs):
        self.profilePic.delete()
        self.resume.delete()
        self.placementGuidelineForm.delete()
        super().delete(*args, **kwargs)


class StudentSchoolDetailModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          auto_created=True, editable=False)
    studentId = models.OneToOneField(StudentPersonalDetailModel, on_delete=models.CASCADE, related_name="school_detail")
    schoolingMedium = models.CharField(max_length=50, choices=SCHOOLING_MEDIUM)
    twelvePercent = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    diplomaPercent = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    tenPercent = models.DecimalField(max_digits=4, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedAt = models.DateTimeField(auto_now_add=False, auto_now=True)


class StudentCollegeDetailModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          auto_created=True, editable=False)
    studentId = models.OneToOneField(StudentPersonalDetailModel, on_delete=models.CASCADE, related_name="college_detail")
    enrollmentNumber = models.CharField(max_length=15, unique=True)
    college = models.CharField(max_length=15)
    branch = models.CharField(max_length=15)
    passingYear = models.IntegerField()
    currentCGPA = models.DecimalField(max_digits=3, decimal_places=2)
    currentBacklog = models.IntegerField(null=True, blank=True, default=None)
    totalBacklog = models.IntegerField(null=True, blank=True, default=None)
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedAt = models.DateTimeField(auto_now_add=False, auto_now=True)
