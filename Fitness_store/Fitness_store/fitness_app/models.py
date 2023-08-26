from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models


def validate_only_alphabetical(value):
    pass


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


class FitnessUser(auth_models.AbstractUser):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )
    GENDER_MAX_LENGTH = 1

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_alphabetical,
        ),

    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_alphabetical,
        ),
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        max_length=GENDER_MAX_LENGTH,
        choices=GENDER_CHOICES,
    )

    profile_picture = models.FileField(
        null=True,
        blank=True,
    )