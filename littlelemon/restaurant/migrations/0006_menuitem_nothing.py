# Generated by Django 4.2.12 on 2024-05-07 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_rename_menu_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='nothing',
            field=models.CharField(default='a', max_length=50),
        ),
    ]
