# Generated by Django 4.2.11 on 2024-05-02 23:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_booking_no_of_guests_alter_menu_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(1)]),
        ),
    ]
