from django.contrib import admin
from Fitness_store.fitness_app.models import BestSellingSupplements, BestSellingGymEquipment


@admin.register(BestSellingSupplements)
class BestSellingSupplements(admin.ModelAdmin):
    pass


@admin.register(BestSellingGymEquipment)
class BestSellingGymEquipment(admin.ModelAdmin):
    pass
