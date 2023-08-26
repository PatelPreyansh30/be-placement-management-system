import uuid
from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class FacultyPersonalModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          auto_created=True, editable=False)
    facultyId = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="facultyDetail")
    address = models.TextField()
    profilePic = models.ImageField(upload_to="faculty_profile_pic/")
    alternateMobile = models.CharField(max_length=150)
    alternateEmail = models.EmailField(max_length=150, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedAt = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.id
    
    def delete(self, *args, **kwargs):
        self.profilePic.delete()
        super().delete(*args, **kwargs)
