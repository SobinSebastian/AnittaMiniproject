# Generated by Django 4.0.3 on 2023-10-02 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horofixapp', '0013_remove_customerprofile_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='street_address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
