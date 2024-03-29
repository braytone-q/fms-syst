from django.db import models
import uuid
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from .managers import CustomUserManager


# user account
class User(AbstractBaseUser, PermissionsMixin):
    # this fields tie to the roles
    ADMIN = 1
    FARMER = 2
    AGRI_EXPERT = 3
    SERVICE_PROVIDER = 4

    ROLE_CHOICES = (
        (ADMIN, "admin"),
        (FARMER, "farmer"),
        (AGRI_EXPERT, "agri_expert"),
        (SERVICE_PROVIDER, "service_provider"),
    )

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    # roles created here
    username = models.CharField(max_length=50, unique=True)
    uid = models.UUIDField(
        unique=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name="Public identifier",
    )
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=30, unique=True)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=False, null=False, default=2
    )
    county = models.CharField(max_length=100, null=True, blank=True)
    farm_location = models.CharField(max_length=100, null=True, blank=True)
    organization = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "role", "phone"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
