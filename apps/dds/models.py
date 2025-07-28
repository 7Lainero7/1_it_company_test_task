from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(max_length=127, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Status(BaseModel):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name


class TransactionType(BaseModel):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=127, unique=True)

    def __str__(self):
        return self.name


class SubCategory(BaseModel):
    name = models.CharField(max_length=127)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        unique_together = ('name', 'category')

    def __str__(self):
        return f"{self.category.name} → {self.name}"


class CashFlowRecord(BaseModel):
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(TransactionType, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.custom_date or self.created_at} — {self.amount} ₽"

