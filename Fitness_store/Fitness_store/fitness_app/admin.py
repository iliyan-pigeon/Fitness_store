from django.contrib import admin
from django.contrib.auth.models import User

from Fitness_store.fitness_app.models import BestSellingSupplements, BestSellingGymEquipment, Supplements, GymEquipment, \
    FitnessUser


@admin.register(BestSellingSupplements)
class BestSellingSupplements(admin.ModelAdmin):
    pass


@admin.register(BestSellingGymEquipment)
class BestSellingGymEquipment(admin.ModelAdmin):
    pass


@admin.register(Supplements)
class Supplements(admin.ModelAdmin):
    pass


@admin.register(GymEquipment)
class GymEquipment(admin.ModelAdmin):
    pass


@admin.register(FitnessUser)
class FitnessUser(admin.ModelAdmin):
    pass

