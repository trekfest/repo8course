# Generated by Django 4.2.4 on 2023-12-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Restaurant", "0003_alter_booking_id_alter_menu_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu", name="inventory", field=models.IntegerField(default=0),
        ),
    ]
