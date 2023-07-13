# Generated by Django 4.1.7 on 2023-06-14 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_remove_cartorder_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='price',
            field=models.DecimalField(decimal_places=2, default='1.99', max_digits=99999999999999),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(decimal_places=2, default='5.00', max_digits=99999999999999),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default='3.00', max_digits=99999999999999),
        ),
    ]
