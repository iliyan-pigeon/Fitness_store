from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import FitnessUser


@receiver(pre_delete, sender=FitnessUser)
def delete_profile_picture(sender, instance, **kwargs):
    if instance.profile_picture:
        instance.profile_picture.delete(save=False)
