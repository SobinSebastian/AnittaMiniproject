# Generated by Django 4.0.3 on 2024-03-18 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horofixapp', '0002_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='watch_customization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='horofixapp.watchcustomization'),
        ),
    ]
