# Generated by Django 4.2.7 on 2023-12-03 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horofixapp', '0005_address_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Placed', 'Placed'), ('Processing', 'Processing'), ('Delivered', 'Delivered')], default='Placed', max_length=20),
        ),
    ]