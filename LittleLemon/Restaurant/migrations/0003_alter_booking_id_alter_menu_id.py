# Generated by Django 4.2.4 on 2023-12-06 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Restaurant", "0002_menuitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="menu",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
