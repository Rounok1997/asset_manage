# Generated by Django 4.1.3 on 2022-12-02 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AssetType",
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
                ("name", models.CharField(max_length=50, null=True)),
                (
                    "company",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
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
                ("employee_id", models.IntegerField(null=True, unique=True)),
                ("employee_name", models.CharField(max_length=100)),
                (
                    "company",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GivenAsset",
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
                (
                    "given_asset_status",
                    models.CharField(
                        choices=[["1", "Unused"], ["2", "Used"], ["3", "New"]],
                        default="3",
                        max_length=20,
                    ),
                ),
                ("asset_given_at", models.DateField(blank=True, null=True)),
                (
                    "returned_asset_status",
                    models.CharField(
                        choices=[
                            ["1", "Unused"],
                            ["2", "Used"],
                            ["3", "Out of date"],
                            ["4", "Damaged"],
                            ["5", "In use"],
                            ["6", "New"],
                            ["7", "lost"],
                            ["8", "stolen"],
                        ],
                        default="6",
                        max_length=20,
                    ),
                ),
                ("asset_returned_at", models.DateField(blank=True, null=True)),
                (
                    "asset",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.assettype",
                    ),
                ),
                (
                    "given_to",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.employee",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="assettype",
            constraint=models.UniqueConstraint(
                fields=("company", "name"), name="unique"
            ),
        ),
    ]
