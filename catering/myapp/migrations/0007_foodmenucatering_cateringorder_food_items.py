# Generated by Django 4.2 on 2025-02-28 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_cateringorder_order_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodMenucatering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('veg', 'Vegetarian'), ('non-veg', 'Non-Vegetarian'), ('dessert', 'Dessert'), ('drinks', 'Drinks')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cateringorder',
            name='food_items',
            field=models.ManyToManyField(to='myapp.foodmenucatering'),
        ),
    ]
