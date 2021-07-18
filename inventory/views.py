from django.db.models import Sum
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import django. utils. timezone as timezone

from store.models import Product, Supplier, Inventory
from users.models import User

import json

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


@login_required(login_url='login')
def dashboard(request):
    inventory_product = Inventory.objects.select_related('product')

    # total of tables
    total_inventory = Inventory.objects.count()
    total_product = Product.objects.count()
    total_supplier = Supplier.objects.count()
    total_user = User.objects.count()

    # Product by time
    lb_years = []
    entry_product_by_year = []
    released_product_by_year = []
    profit_by_year = []
    for i in range(0, 5):
        year = timezone.now().year - i
        lb_years.append(year)
        entry_product_by_year.append(Inventory.objects.filter(created_at__year=year, qty__gte=0).aggregate(Sum('qty')).get('qty__sum'))
        released_product_by_year.append(Inventory.objects.filter(created_at__year=year, qty__lt=0).aggregate(Sum('qty')).get('qty__sum'))

        tmp = list(Inventory.objects.filter(created_at__year=year, qty__lt=0).values_list('product', 'qty'))
        sum_profit = 0
        for out in tmp:
            p = Product.objects.filter(pk=out[0]).first()
            sum_profit = sum_profit + (p.buying_price - p.selling_price)*out[1]
        profit_by_year.append(sum_profit)

    lb_years.reverse()
    entry_product_by_year.reverse()
    released_product_by_year.reverse()
    profit_by_year.reverse()

    lb_months = []
    entry_product_by_month = []
    released_product_by_month = []
    profit_by_month = []
    for i in range(0, 5):
        month = timezone.now().month - i
        lb_months.append(month)
        entry_product_by_month.append(Inventory.objects.filter(created_at__month=month, qty__gte=0).aggregate(Sum('qty')).get('qty__sum'))
        released_product_by_month.append(Inventory.objects.filter(created_at__month=month, qty__lt=0).aggregate(Sum('qty')).get('qty__sum'))

        tmp = list(Inventory.objects.filter(created_at__month=month, qty__lt=0).values_list('product', 'qty'))
        sum_profit = 0
        for out in tmp:
            p = Product.objects.filter(pk=out[0]).first()
            sum_profit = sum_profit + (p.buying_price - p.selling_price)*out[1]
        profit_by_month.append(sum_profit)

    lb_months.reverse()
    entry_product_by_month.reverse()
    released_product_by_month.reverse()
    profit_by_month.reverse()

    # Product by category
    all_categories = Product.objects.values_list('category')
    filtered_categories = []
    for category in all_categories:
        if category not in filtered_categories:
            filtered_categories.append(category)

    lb_categories = []
    entry_product_by_category = []
    released_product_by_category = []
    total_product_by_category = []
    for category in filtered_categories:
        lb_categories.append(category[0])
        total_product_by_category.append(Product.objects.filter(category=category[0]).count())
        entry_product_by_category.append(inventory_product.filter(product__category=category[0], qty__gte=0).aggregate(Sum('qty')).get('qty__sum'))
        released_product_by_category.append(inventory_product.filter(product__category=category[0], qty__lt=0).aggregate(Sum('qty')).get('qty__sum'))

    # Product by designation
    all_product_designation = Product.objects.values_list('designation')
    filtered_product_designation = []
    for designation in all_product_designation:
        if designation not in filtered_product_designation:
            filtered_product_designation.append(designation)

    lb_designations = []
    total_product_by_designation = []
    entry_product_by_designation = []
    released_product_by_designation = []
    for designation in filtered_product_designation:
        lb_designations.append(designation[0])
        total_product_by_designation.append(Product.objects.filter(designation=designation[0]).count())
        entry_product_by_designation.append(inventory_product.filter(product__designation=designation[0], qty__gte=0).aggregate(Sum('qty')).get('qty__sum'))
        released_product_by_designation.append(inventory_product.filter(product__designation=designation[0], qty__lt=0).aggregate(Sum('qty')).get('qty__sum'))

    context = {
        'total_inventory': total_inventory,
        'total_product': total_product,
        'total_supplier': total_supplier,
        'total_user': total_user,
        'lb_years': lb_years,
        'entry_product_by_year': clean_list(entry_product_by_year),
        'released_product_by_year': abs_list(clean_list(released_product_by_year)),
        'profit_by_year': profit_by_year,
        'lb_months': lb_months,
        'entry_product_by_month': clean_list(entry_product_by_month),
        'released_product_by_month': abs_list(clean_list(released_product_by_month)),
        'profit_by_month': profit_by_month,
        'lb_categories': json.dumps(lb_categories),
        'total_product_by_category': clean_list(total_product_by_category),
        'entry_product_by_category': clean_list(entry_product_by_category),
        'released_product_by_category': abs_list(clean_list(released_product_by_category)),
        'lb_designations': json.dumps(lb_designations),
        'total_product_by_designation': clean_list(total_product_by_designation),
        'entry_product_by_designation': clean_list(entry_product_by_designation),
        'released_product_by_designation': abs_list(clean_list(released_product_by_designation)),
    }
    return render(request, 'dashboard.html', context)

def clean_list(li):
    result = []
    for i in li:
        result.append(0 if i is None else i)
    return result

def abs_list(li):
    result = []
    for i in li:
        result.append(-i if i < 0 else i)
    return result