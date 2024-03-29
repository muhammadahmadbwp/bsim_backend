from django.db import models
import uuid
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from adminpanel.models import AdminsDetail
from clientpanel.models import ClientsDetail
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        super_admin = Role.objects.get(user_role='SUPER_ADMIN')
        extra_fields.setdefault('role', super_admin)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Role(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    user_role = models.CharField(max_length=50)

    def __str__(self):
        return self.user_role

class User(AbstractBaseUser, PermissionsMixin):
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='public identifier')
    username = models.CharField(unique=True, max_length=50, null=False, blank=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30, unique=True, blank=True, null=True)
    password = models.CharField(max_length=128)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='user_roles')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    otp = models.CharField(max_length=4, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)

    REQUIRED_FIELDS = ['username', 'password']
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.username

@receiver(post_save, sender=User, dispatch_uid="create_user_detail")
def create_user_detail(sender, instance, **kwargs):
    if instance.role.user_role == 'ADMIN':
        AdminsDetail.objects.create(user=instance)
    # if instance.role.user_role == 'CLIENT':
    #     ClientsDetail.objects.create(user=instance)