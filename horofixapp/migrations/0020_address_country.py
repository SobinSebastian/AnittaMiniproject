# Generated by Django 4.0.3 on 2024-03-13 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horofixapp', '0019_remove_address_country_remove_address_is_default_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]