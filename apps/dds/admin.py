from django.contrib import admin
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper

from apps.dds.form import CashFlowRecordForm
from apps.dds.models import (
    CashFlowRecord,
    Category,
    Status,
    SubCategory,
    TransactionType,
)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "type")
    list_filter = ("type",)
    search_fields = ("name",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(CashFlowRecord)
class CashFlowRecordAdmin(admin.ModelAdmin):
    form = CashFlowRecordForm

    list_display = (
        "created_at",
        "status",
        "type",
        "category",
        "subcategory",
        "amount",
        "comment",
    )
    autocomplete_fields = ['category', 'subcategory']
    list_filter = ("created_at", "status", "type", "category", "subcategory")
    search_fields = ("comment",)
    date_hierarchy = "created_at"

    class Media:
        js = (
            'admin/js/vendor/jquery/jquery.min.js',
            'admin/js/filter_subcategories.js',
        )
