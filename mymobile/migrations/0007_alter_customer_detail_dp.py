# Generated by Django 4.1.5 on 2023-01-31 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymobile', '0006_customer_detail_dp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_detail',
            name='dp',
            field=models.ImageField(default='mydp.jpeg', upload_to='photos'),
        ),
    ]
