# Generated by Django 4.2 on 2025-02-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_order_order_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cateringorder',
            name='order_type',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
