from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, Permission, Group
from django.core import validators
from django.db import models
from django.contrib.auth.models import User as DefaultUser, Permission


class BestSellingSupplements(models.Model):

    name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
        ),
    )

    description = models.TextField(
        null=False,
        blank=False,
        max_length=300,
        validators=(
            validators.MinLengthValidator(5),
        ),
    )

    photo = models.FileField(
        null=False,
        blank=False,
        upload_to='best_products_images'
    )


class BestSellingGymEquipment(models.Model):

    name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
        ),
    )

    description = models.TextField(
        null=False,
        blank=False,
        max_length=300,
        validators=(
            validators.MinLengthValidator(5),
        ),
    )

    photo = models.FileField(
        null=False,
        blank=False,
        upload_to='best_products_images'
    )


class Supplements(models.Model):

    name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
        ),
    )

    amount = models.IntegerField(
        null=False,
        blank=False,
    )

    amount_type = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )

    photo = models.FileField(
        null=False,
        blank=False,
        upload_to='supplements',
        default=None,
    )


class GymEquipment(models.Model):

    name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
        ),
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )

    photo = models.FileField(
        null=False,
        blank=False,
        upload_to='gym_equipment',
        default=None,
    )


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, is_staff=False, is_superuser=False):
        if not username:
            raise ValueError("The Username field must be set.")
        user = self.model(username=username, is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)


class CustomUser(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(
        max_length=150,
        unique=True,
    )
    email = models.EmailField(unique=True,)
    is_active = models.BooleanField(default=True,)
    is_staff = models.BooleanField(default=False,)
    is_superuser = models.BooleanField(default=False)

    # Specify the field used as the unique identifier for the user
    USERNAME_FIELD = 'username'

    # Here are the fields required for creating a user via the createsuperuser management command.
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='custom_users',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='custom_users_permissions',
    )

    def __str__(self):
        return self.username


class ProfileModel(models.Model):
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    first_name = models.CharField(
        max_length=34,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=34,
        blank=True,
        null=True,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    gender = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=CHOICES,
    )

    image = models.FileField(
        upload_to='profile_pics',
        blank=True,
        null=True,
    )

    profile = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
    )

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return None

    def __str__(self):
        return f'{self.id} {self.get_full_name()}'
