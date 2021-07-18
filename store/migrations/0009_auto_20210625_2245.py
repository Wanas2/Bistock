# Generated by Django 3.0.8 on 2021-06-25 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0008_inventory_recordmovement_supplyproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplyproduct',
            name='product',
        ),
        migrations.RemoveField(
            model_name='supplyproduct',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='location',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='inventory',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.Product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventory',
            name='supplier',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.Supplier'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventory',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='designation',
            field=models.CharField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='email',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.DeleteModel(
            name='RecordMovement',
        ),
        migrations.DeleteModel(
            name='SupplyProduct',
        ),
    ]
