# Generated by Django 4.1.4 on 2023-05-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_vendor_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, default='Morando', max_length=100, null=True),
        ),
    ]
