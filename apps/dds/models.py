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
