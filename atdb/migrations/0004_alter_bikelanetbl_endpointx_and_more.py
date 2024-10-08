# Generated by Django 5.1 on 2024-10-10 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("atdb", "0003_bikelanetbl_province"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bikelanetbl",
            name="EndPointX",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="bikelanetbl",
            name="EndPointY",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="bikelanetbl",
            name="Length",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="bikelanetbl",
            name="StartPointX",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="bikelanetbl",
            name="StartPointY",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
