# Generated by Django 4.2.7 on 2023-11-30 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horofixapp', '0003_rename_customer_customerprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='pincode',
        ),
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
