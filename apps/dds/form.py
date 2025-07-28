from django.core.exceptions import ValidationError
from django import forms
from .models import CashFlowRecord, Category, SubCategory


class CategorySelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            try:
                category_id = value.value
                category = Category.objects.get(pk=category_id)
                option["attrs"]["data-type-id"] = category.type_id
            except Category.DoesNotExist:
                pass
        return option


class SubCategorySelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            try:
                subcategory_id = value.value
                subcategory = SubCategory.objects.get(pk=subcategory_id)
                option["attrs"]["data-category-id"] = subcategory.category_id
            except SubCategory.DoesNotExist:
                pass
        return option
  

class CashFlowRecordForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.select_related("type"),
        widget=CategorySelect
    )
    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.select_related("category"),
        widget=SubCategorySelect
    )

    class Meta:
        model = CashFlowRecord
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get("category")
        subcategory = cleaned_data.get("subcategory")
        type_ = cleaned_data.get("type")

        if subcategory and category and subcategory.category != category:
            raise ValidationError({"subcategory": "Подкатегория не принадлежит выбранной категории."})

        if category and type_ and category.type != type_:
            raise ValidationError({"category": "Категория не принадлежит выбранному типу."})

        return cleaned_data
