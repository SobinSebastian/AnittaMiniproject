# Generated by Django 5.0.3 on 2024-04-06 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horofixapp', '0012_cartitem_customization_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='customization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='horofixapp.customizationdetail'),
        ),
    ]
