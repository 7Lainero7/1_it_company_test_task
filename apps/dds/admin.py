from django.contrib import admin

from apps.dds.models import (
    Status,
    TransactionType,
    Category,
    SubCategory,
    CashFlowRecord
)


admin.site.register(Status)
admin.site.register(TransactionType)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(CashFlowRecord)
