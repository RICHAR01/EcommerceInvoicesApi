from users.models import User
from django.db import models
from base.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Subcategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Subcategories"


class Brand(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class MeasureUnit(BaseModel):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"


class Product(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=50, unique=True)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_min = models.IntegerField(default=0)
    stock_max = models.IntegerField(default=0)
    current_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name