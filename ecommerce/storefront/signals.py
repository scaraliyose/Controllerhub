# storefront/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Review

@receiver(post_save, sender=Review)
def review_saved(sender, instance, **kwargs):
    instance.product.update_rating_cache()

@receiver(post_delete, sender=Review)
def review_deleted(sender, instance, **kwargs):
    instance.product.update_rating_cache()
