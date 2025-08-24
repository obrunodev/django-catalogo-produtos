from apps.products.models import Product
from django import forms


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'value', 'promotional_value']
