from django.contrib import admin
from django.contrib.auth.models import User

from Fitness_store.fitness_app.models import Supplements, GymEquipment, \
    FitnessUser, Cart, CartItem


@admin.register(Supplements)
class Supplements(admin.ModelAdmin):
    pass


@admin.register(GymEquipment)
class GymEquipment(admin.ModelAdmin):
    pass


@admin.register(FitnessUser)
class FitnessUser(admin.ModelAdmin):
    pass


@admin.register(Cart)
class Cart(admin.ModelAdmin):
    pass


@admin.register(CartItem)
class CartItem(admin.ModelAdmin):
    pass
