from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.core.exceptions import ValidationError

from .models import CashFlowRecord, Category, SubCategory


def wrap_if_needed(widget, rel, admin_site):
    if isinstance(widget, RelatedFieldWidgetWrapper):
        return widget
    return RelatedFieldWidgetWrapper(widget, rel, admin_site)


class CategorySelect(forms.Select):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_map = {
            str(cat.pk): cat.type_id for cat in Category.objects.only("id", "type_id")
        }

    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        option = super().create_option(
            name, value, label, selected, index, subindex, attrs
        )
        type_id = self._type_map.get(str(value))
        if type_id is not None:
            option["attrs"]["data-type-id"] = type_id
        return option


class SubCategorySelect(forms.Select):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._category_map = {
            str(sub.pk): sub.category_id
            for sub in SubCategory.objects.only("id", "category_id")
        }

    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        option = super().create_option(
            name, value, label, selected, index, subindex, attrs
        )
        category_id = self._category_map.get(str(value))
        if category_id is not None:
            option["attrs"]["data-category-id"] = category_id
        return option


class CashFlowRecordForm(forms.ModelForm):
    class Meta:
        model = CashFlowRecord
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        rel_category = CashFlowRecord._meta.get_field("category").remote_field
        self.fields["category"].widget = wrap_if_needed(
            self.fields["category"].widget, rel_category, admin.site
        )

        rel_subcategory = CashFlowRecord._meta.get_field("subcategory").remote_field
        self.fields["subcategory"].widget = wrap_if_needed(
            self.fields["subcategory"].widget, rel_subcategory, admin.site
        )

    def clean(self):
        cleaned_data = super().clean()
        type = cleaned_data.get("type")
        category = cleaned_data.get("category")
        subcategory = cleaned_data.get("subcategory")

        if category and type and category.type_id != type.id:
            raise ValidationError("Выбранная категория не относится к выбранному типу.")

        if subcategory and category and subcategory.category_id != category.id:
            raise ValidationError(
                "Выбранная подкатегория не относится к выбранной категории."
            )

        return cleaned_data
