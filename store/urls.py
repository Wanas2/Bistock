from django.urls import path

from .views import (
    create_supplier,
    modify_supplier,
    delete_supplier,
    SupplierListView,

    create_product,
    modify_product,
    delete_product,
    ProductListView,

    InventoryView,
    add_inventory,
    delete_inventory
)

urlpatterns = [
    # supplier urls
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('modify-supplier/<supplier_id>', modify_supplier, name='modify-supplier'),
    path('delete-supplier/<supplier_id>', delete_supplier, name='delete-supplier'),
    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),

    # product urls
    path('create-product/', create_product, name='create-product'),
    path('modify-product/<product_id>', modify_product, name='modify-product'),
    path('delete-product/<product_id>', delete_product, name='delete-product'),
    path('product-list/', ProductListView.as_view(), name='product-list'),

    # inventory urls
    path('inventory/', InventoryView.as_view(), name='inventory'),
    path('add-inventory/', add_inventory, name='add_inventory'),
    path('delete-inventory/<inventory_id>', delete_inventory, name='delete_inventory'),

]
