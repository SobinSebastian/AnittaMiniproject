# Generated by Django 4.0.3 on 2024-03-13 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('horofixapp', '0020_address_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchproduct',
            name='category',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids'), ('Unisex', 'Unisex')], default=None, max_length=10),
        ),
        migrations.CreateModel(
            name='CustomizationPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razor_pay_order_id', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('is_paid', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horofixapp.watchcustomization')),
            ],
        ),
    ]