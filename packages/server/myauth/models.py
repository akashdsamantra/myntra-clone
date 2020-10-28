from django.db import models
from django.contrib.auth.models import AbstractBaseUser

GENDER_OPTIONS = [('m', 'Male'), ('f', 'Female'), ('o', 'Other')]
OTP_TYPE_CHOICES = [
    ('mobile-verification', 'Mobile Verification'),
    ('email-verification', 'Email Verification'),
    ('mobile-login', 'Mobile Login'),
    ('forgot-password', 'Forgot Password')
]

# Create your models here.
class User(AbstractBaseUser):
    mobile = models.CharField(max_length=10)
    first_name = models.CharField(max_length=256, null=True, blank=True)
    middle_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=GENDER_OPTIONS, max_length=1, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    is_mobile_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

class OTP(models.Model):
    user = models.ForeignKey(User, related_name="otps", on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    code = models.CharField(max_length=10)
    type = models.CharField(choices=OTP_TYPE_CHOICES, max_length=50)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ' - ' + self.type
