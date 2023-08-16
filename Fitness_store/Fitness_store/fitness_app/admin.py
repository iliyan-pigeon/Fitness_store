from django.contrib import admin
from Fitness_store.fitness_app.models import BestSellingSupplements, BestSellingGymEquipment, Supplements, GymEquipment, \
    CustomUser


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


@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    pass
