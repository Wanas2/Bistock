from django import forms

from .models import Product, Supplier, Inventory


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'address', 'email', 'tel']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'data-val': 'true',
                'data-val-required': 'Please enter name',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'address',
                'data-val': 'true',
                'data-val-required': 'Please enter address',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'data-val': 'true',
                'data-val-required': 'Please enter email',
            }),
            'tel': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'tel',
                'data-val': 'true',
                'data-val-required': 'Please enter telephone',
            }),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['designation', 'buying_price', 'selling_price', 'category']
        widgets = {
            'designation': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'designation'
            }),
            'buying_price': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'buying_price'
            }),
            'selling_price': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'selling_price'
            }),
            'category': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'category'
            })
        }


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['user', 'product', 'supplier', 'qty', 'created_at']
        widgets = {
            'created_at': forms.DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(InventoryForm, self).__init__(*args, **kwargs)
        for v in self.visible_fields():
            v.field.widget.attrs['class'] = 'form-control'
