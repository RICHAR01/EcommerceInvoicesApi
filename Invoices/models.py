from django.db import models
from base.models import BaseModel

# Create your models here.
class Client(BaseModel):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    client_type = models.CharField(max_length=50, choices=[('individual', 'Individual'), ('company', 'Company')], default='individual')

    def __str__(self):
        return f"{self.name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Clients"
        
    


class SaleHeader(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice_date = models.DateField()
    subtotal = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    total_amount = models.FloatField(default=0)
    invoice_status = models.CharField(max_length=50, choices=[('uninvoiced', 'Uninvoiced'), ('invoiced', 'Invoiced')], default='uninvoiced')
    paid_status = models.CharField(max_length=50, choices=[('unpaid', 'Unpaid'), ('paid', 'Paid')], default='unpaid')

    def __str__(self):
        return f"Invoice {self.id} - {self.client.name}"

    class Meta:
        verbose_name_plural = "Invoices"
        
        
class SaleDetail(BaseModel):
    sale = models.ForeignKey(SaleHeader, on_delete=models.CASCADE, related_name='sale_details')
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.FloatField(default=0)
    line_subtotal = models.FloatField(default=0)
    line_discount = models.FloatField(default=0)
    line_total = models.FloatField(default=0)

    def __str__(self):
        return f"SaleDetail {self.id} - {self.product}"

    class Meta:
        verbose_name_plural = "Sale Details"
