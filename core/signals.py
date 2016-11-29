from django.db.models.signals import post_save

from core.models import Purchase


def purchase_post_save(sender, instance=None, created=False, **kwargs):
    if created:
        product = instance.product
        product.amount -= instance.amount_to_sell
        product.save()


post_save.connect(purchase_post_save, sender=Purchase)