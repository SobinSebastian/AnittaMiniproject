# Generated by Django 4.0.3 on 2023-10-04 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horofixapp', '0017_watchproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchproduct',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='horofixapp.category'),
        ),
    ]
