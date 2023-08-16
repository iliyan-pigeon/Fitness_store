from django.core import validators
from django.db import models


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


