from django.core.exceptions import ValidationError
from django import forms
from .models import CashFlowRecord


class CashFlowRecordForm(forms.ModelForm):
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
