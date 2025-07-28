from django.contrib import admin
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper

from apps.dds.form import CashFlowRecordForm, CategorySelect, SubCategorySelect
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
    list_filter = ("created_at", "status", "type", "category", "subcategory")
    search_fields = ("comment",)
    date_hierarchy = "created_at"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Для поля category
        if db_field.name == "category":
            kwargs["widget"] = RelatedFieldWidgetWrapper(
                CategorySelect(),  # ваш кастомный виджет
                db_field.remote_field,  # связь с моделью
                self.admin_site,  # текущая админка
                can_add_related=True,  # разрешаем добавлять новые
            )

        # Для поля subcategory
        elif db_field.name == "subcategory":
            kwargs["widget"] = RelatedFieldWidgetWrapper(
                SubCategorySelect(),  # ваш кастомный виджет
                db_field.remote_field,
                self.admin_site,
                can_add_related=True,
            )

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = ("admin/js/filter_subcategories.js",)
