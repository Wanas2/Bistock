from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from users.models import User
from .models import (
    Supplier,
    Product,
    Inventory
)
from .forms import (
    SupplierForm,
    ProductForm,
    InventoryForm
)

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Supplier views
@login_required(login_url='login')
def create_supplier(request):
    forms = SupplierForm()
    if request.method == 'POST':
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            tel = forms.cleaned_data['tel']
            Supplier.objects.create(name=name, address=address, email=email, tel=tel)
            return redirect('supplier-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_supplier.html', context)


@login_required(login_url='login')
def modify_supplier(request, supplier_id):
    supplier = Supplier.objects.filter(pk=supplier_id).first()
    forms = SupplierForm(instance=supplier)
    logger.error(forms)
    if request.method == 'POST':
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            tel = forms.cleaned_data['tel']
            Supplier.objects.filter(pk=supplier_id).update(name=name, address=address, email=email, tel=tel)
            return redirect('supplier-list')
    context = {
        'form': forms
    }
    return render(request, 'store/modify_supplier.html', context)


@login_required(login_url='login')
def delete_supplier(request, supplier_id):
    try:
        Supplier.objects.filter(id=supplier_id).delete()
        messages.success(request, "delete supplier successfully")
    except:
        messages.error(request, "delete supplier failed!!!")
    return render(request, 'store/supplier_list.html')


class SupplierListView(ListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
    context_object_name = 'supplier'


# Product views
@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_product.html', context)


@login_required(login_url='login')
def modify_product(request, product_id):
    product = Product.objects.filter(pk=product_id).first()
    forms = ProductForm(instance=product)
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            designation = forms.cleaned_data['designation']
            buying_price = forms.cleaned_data['buying_price']
            selling_price = forms.cleaned_data['selling_price']
            category = forms.cleaned_data['category']
            Product.objects.filter(pk=product_id).update(
                designation=designation,
                buying_price=buying_price,
                selling_price=selling_price,
                category=category
            )
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'store/modify_product.html', context)


@login_required(login_url='login')
def delete_product(request, product_id):
    try:
        Product.objects.filter(id=product_id).delete()
        messages.success(request, "delete product successfully")
    except:
        messages.error(request, "delete product failed!!!")

    return render(request, 'store/product_list.html')


class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'product'


# Inventory views

class InventoryView(ListView):
    model = Inventory
    template_name = 'store/inventory.html'
    context_object_name = 'inventory'

@login_required(login_url='login')
def add_inventory(request):
    forms = InventoryForm()
    if request.method == 'POST':
        forms = InventoryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('inventory')
    context = {
        'form': forms
    }
    return render(request, 'store/add_inventory.html', context)

@login_required(login_url='login')
def delete_inventory(request, inventory_id):
    try:
        Inventory.objects.filter(id=inventory_id).delete()
        messages.success(request, "delete inventory successfully")
    except:
        messages.error(request, "delete inventory failed!!!")
    finally:
        return render(request, 'store/inventory.html')
