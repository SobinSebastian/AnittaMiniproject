# Generated by Django 5.0.3 on 2024-04-09 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horofixapp', '0018_cart_customization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(choices=[('Placed', 'Placed'), ('Processing', 'Processing'), ('Delivered', 'Delivered'), ('Out for Delivery', 'Out for Delivery')], default='Placed', max_length=20),
        ),
    ]
