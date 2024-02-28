# Generated by Django 4.2.7 on 2024-02-21 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horofixapp', '0002_repairpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairpayment',
            name='payment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Failed', 'Failed')], default='Pending', max_length=20),
        ),
    ]