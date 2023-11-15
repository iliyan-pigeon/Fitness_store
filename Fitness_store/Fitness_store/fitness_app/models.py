from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models
from django.utils import timezone


def validate_only_alphabetical(value):
    pass


class Supplements(models.Model):

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

    best_selling = models.BooleanField(
        null=False,
        blank=False,
        default=False,
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

    amount_in_stock = models.PositiveIntegerField(
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

    description = models.TextField(
        null=False,
        blank=False,
        max_length=300,
        validators=(
            validators.MinLengthValidator(5),
        ),
    )

    best_selling = models.BooleanField(
        null=False,
        blank=False,
        default=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )

    amount_in_stock = models.PositiveIntegerField(
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
        upload_to='profile_pictures',
        default=None,
    )


class Cart(models.Model):
    user = models.ForeignKey(FitnessUser, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    session_key = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        if self.user:
            return f"Cart for {self.user.username}"
        return "Guest Cart"

    @classmethod
    def get_cart_for_user_or_session(cls, user=None, session_key=None):
        if user:
            return cls.objects.get_or_create(user=user)[0]
        elif session_key:
            return cls.objects.get_or_create(session_key=session_key)[0]
        return None


class CartItem(models.Model):
    MAX_LENGTH_NAME = 30
    MAX_DIGITS_PRICE = 10
    DECIMAL_PLACES = 2
    DEFAULT_QUANTITY = 1

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    name = models.CharField(max_length=MAX_LENGTH_NAME)
    price = models.DecimalField(max_digits=MAX_DIGITS_PRICE, decimal_places=DECIMAL_PLACES)
    quantity = models.PositiveIntegerField(default=DEFAULT_QUANTITY)
    product_id = models.PositiveIntegerField(default=DEFAULT_QUANTITY)
    product_type = models.CharField(max_length=MAX_LENGTH_NAME, default='')

    def __str__(self):
        return f"{self.quantity} x {self.name}"


class Order(models.Model):
    PENDING = 'Pending'
    DELIVERED = 'Delivered'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    ]

    user = models.ForeignKey(FitnessUser, on_delete=models.SET_NULL, blank=True, null=True)
    session_key = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f"{self.address}"


class OrderItem(models.Model):
    MAX_LENGTH_NAME = 30
    MAX_DIGITS_PRICE = 10
    DECIMAL_PLACES = 2
    DEFAULT_QUANTITY = 1

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=MAX_LENGTH_NAME)
    price = models.DecimalField(max_digits=MAX_DIGITS_PRICE, decimal_places=DECIMAL_PLACES)
    quantity = models.PositiveIntegerField(default=DEFAULT_QUANTITY)
    product_id = models.PositiveIntegerField(default=DEFAULT_QUANTITY)
    product_type = models.CharField(max_length=MAX_LENGTH_NAME, default='')

    def __str__(self):
        return f"{self.quantity} x {self.name} in Order #{self.order}"
