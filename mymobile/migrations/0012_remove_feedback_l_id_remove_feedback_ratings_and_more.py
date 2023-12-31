# Generated by Django 4.1.5 on 2023-02-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymobile', '0011_product_detail_pro_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='L_id',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='Ratings',
        ),
        migrations.AddField(
            model_name='feedback',
            name='Email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Comment',
            field=models.CharField(default='', max_length=250),
        ),
    ]
