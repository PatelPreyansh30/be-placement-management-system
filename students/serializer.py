from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class StudentSerializer(ModelSerializer):
    class Meta:
        model = models.StudentModel
        fields = '__all__'
        extra_kwargs = {
            'whatsappMobile': {
                'error_messages': {
                    'blank': "Whatsapp number is required",
                }
            },
            'alternateMobile': {
                'error_messages': {
                    'blank': "Alternate number is required",
                },
                # 'validators': [
                #     UniqueValidator(
                #         queryset=User.objects.all(),
                #         message="Mobile number already exists"
                #     )
                # ]
            },
            'address': {
                'error_messages': {
                    'blank': "Address is required",
                }
            },
            'profilePic': {
                'error_messages': {
                    'blank': "Profile picture is required",
                    "required": "Profile picture is required",
                }
            },
            'resume': {
                'error_messages': {
                    'blank': "Resume is required",
                }
            },
            'placementGuidelineForm': {
                'error_messages': {
                    'blank': "Placement guidelines form is required",
                }
            },
            'schoolMedium': {
                'error_messages': {
                    'blank': "School medium is required",
                }
            },
            'twelvePercent': {
                'error_messages': {
                    'blank': "Twelve percentage is required",
                    'invalid': "Enter valid twelve percentage",
                }
            },
            'diplomaPercent': {
                'error_messages': {
                    'blank': "Diploma percentage is required",
                    'invalid': "Enter valid diploma percentage",
                }
            },
            'tenPercent': {
                'error_messages': {
                    'blank': "Ten percentage is required",
                    'invalid': "Enter valid ten percentage",
                }
            },
            'enrollmentNumber': {
                'error_messages': {
                    'blank': "Enrollment number is required",
                }
            },
            'college': {
                'error_messages': {
                    'blank': "College is required",
                }
            },
            'branch': {
                'error_messages': {
                    'blank': "Branch is required",
                }
            },
            'passingYear': {
                'error_messages': {
                    'blank': "Passing year is required",
                    'invalid': "Enter valid passing year",
                }
            },
            'currentCGPA': {
                'error_messages': {
                    'blank': "Current CGPA is required",
                    'invalid': "Enter valid current CGPA",
                }
            },
            'studentId': {
                'error_messages': {
                    'blank': "Student id is required",
                }
            },
        }

    def update(self, instance, validated_data):
        new_resume = validated_data.get('resume')
        new_profile_pic = validated_data.get('profilePic')
        new_guideline_form = validated_data.get('placementGuidelineForm')
        if new_resume:
            instance.resume.delete()
            instance.resume = new_resume
        if new_profile_pic:
            instance.profilePic.delete()
            instance.profilePic = new_profile_pic
        if new_guideline_form:
            instance.placementGuidelineForm.delete()
            instance.placementGuidelineForm = new_guideline_form
        instance.save()
        return instance


class StudentDetailedSerializer(ModelSerializer):
    studentDetail = StudentSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'studentDetail',
                  'mobile', 'email', 'isStudent', 'isStaff']
