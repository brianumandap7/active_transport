# Generated by Django 5.1 on 2024-09-12 23:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("atdb", "0008_fundsource_alter_bikelanetbl_fundsource"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TypeofworkAuditLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("old_value", models.CharField(blank=True, max_length=255, null=True)),
                ("new_value", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "edited_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "typeofwork",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="atdb.typeofwork",
                    ),
                ),
            ],
        ),
    ]