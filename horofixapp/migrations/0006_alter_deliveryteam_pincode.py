# Generated by Django 4.2.7 on 2023-11-29 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horofixapp', '0005_remove_deliveryteam_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryteam',
            name='pincode',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
