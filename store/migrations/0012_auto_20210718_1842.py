# Generated by Django 3.0.8 on 2021-07-18 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20210626_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 7, 18, 18, 42, 28, 556234)),
        ),
    ]
