# Generated by Django 5.1 on 2024-09-20 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("atdb", "0017_alter_bikelanetbl_bikedate"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bikearea",
            options={"permissions": [("edit_bikearea", "Can change bike area")]},
        ),
    ]
