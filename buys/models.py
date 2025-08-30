from django.db import models
from base.models import BaseModel
from inv.models import Product

class Supplier(BaseModel):
    description = models.CharField(max_length=100, unique=True)
    adress = models.CharField(max_length=250, null=True, blank=True)
    contact = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.description = self.description.upper()
        super(Supplier, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Suppliers"


class BuyHeader(BaseModel):
    buy_date = models.DateField()
    observation = models.TextField(blank=True, null=True)
    invoice = models.CharField(max_length=100)
    invoice_date = models.DateField()
    subtotal = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    total = models.FloatField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.observation

    def save(self, *args, **kwargs):
        self.observation = self.observation.upper()
        super(BuyHeader, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Buy Headers"


class BuyDetail(BaseModel):
    buy = models.ForeignKey(BuyHeader, related_name='buy_details', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    supply_price = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return str(self.product)

    def save(self, *args, **kwargs):
        super(BuyDetail, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Buy Details"