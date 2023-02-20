from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class CustomUser(AbstractBaseUser):
    username = models.CharField(verbose_name="username", max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD ='username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):

        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Booking(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=True)
    last_name = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(verbose_name="booking_email", blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    choice = models.CharField(max_length=100, blank=False, null=True)
    address = models.TextField(blank=False)
    city = models.CharField(max_length=100, blank=False, null=True)
    state = models.CharField(max_length=100, blank=False, null=True)
    country = models.CharField(max_length=100, blank=False, null=True)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name