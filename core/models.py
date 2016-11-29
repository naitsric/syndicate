from django.db import models


class Product(models.Model):
    product_id = models.CharField(max_length=30)
    type = models.CharField(max_length=30, choices=(('advance', 'Advance'),))
    date = models.DateField(verbose_name='Date')
    amount = models.DecimalField(max_digits=10, decimal_places=3)


class Investor(models.Model):
    name = models.CharField(max_length=30)


class Purchase(models.Model):
    investor = models.ForeignKey(Investor)
    product = models.ForeignKey(Product)
    amount_to_sell = models.DecimalField(max_digits=10, decimal_places=3)
    left_amount = models.DecimalField(max_digits=10, decimal_places=3)
