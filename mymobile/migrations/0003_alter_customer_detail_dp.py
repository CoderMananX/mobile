# Generated by Django 4.1.5 on 2023-01-31 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymobile', '0002_product_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_detail',
            name='Dp',
            field=models.ImageField(default='photos/mydp.jpeg', upload_to='photos'),
        ),
    ]