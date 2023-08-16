# Generated by Django 4.1.4 on 2022-12-29 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymobile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_order',
            name='order_status',
            field=models.CharField(choices=[('pending', 'PENDING'), ('deliverd', 'DELIVERD')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
