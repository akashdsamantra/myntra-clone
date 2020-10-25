from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
  mobile = models.CharField(max_length=10)
  first_name = models.CharField(max_length=256)
  middle_name = models.CharField(max_length=256)
  last_name = models.CharField(max_length=256)
  email = models.EmailField()
  gender = models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], max_length=1)
  dob = models.DateField()
  is_mobile_verified = models.BooleanField(default=False)
  is_email_verified = models.BooleanField(default=False)

OTP_TYPE_CHOICES = [
  ('mobile-verification', 'Mobile Verification'), 
  ('email-verification', 'Email Verification'), 
  ('mobile-login', 'Mobile Login'), 
  ('forgot-password', 'Forgot Password')
]

class OTP(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  email = models.EmailField()
  mobile = models.CharField(max_length=10)
  code = models.CharField(max_length=10)
  type = models.CharField(choices=OTP_TYPE_CHOICES, max_length=50)
  created = models.DateField(auto_now=True)