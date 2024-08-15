# Generated by Django 5.1 on 2024-08-09 07:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("atdb", "0007_bikeclass_alter_bikelanetbl_bikeclass"),
    ]

    operations = [
        migrations.CreateModel(
            name="FundSource",
            fields=[
                ("FundSource_id", models.AutoField(primary_key=True, serialize=False)),
                ("FundSource", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name="bikelanetbl",
            name="FundSource",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="FundSource_name",
                to="atdb.fundsource",
            ),
        ),
    ]