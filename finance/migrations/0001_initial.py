# Generated by Django 5.0.6 on 2024-06-11 16:56

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0003_staffmember_reports_to"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExpenseCategory",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="ExpenseStatus",
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
                ("status", models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name="ItemizedExpense",
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
                ("vendor", models.CharField(max_length=100)),
                ("reason", models.CharField(max_length=100)),
                ("date_of_transaction", models.DateField()),
                ("value", models.DecimalField(decimal_places=2, max_digits=10)),
                ("note", models.TextField(blank=True, null=True)),
                ("receipt", models.ImageField(upload_to="")),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="finance.expensecategory",
                    ),
                ),
                (
                    "purchaser",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.staffmember",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExpenseApproval",
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
                ("review_date", models.DateField(default=datetime.date.today)),
                (
                    "reviewed_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.staffmember",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="finance.expensestatus",
                    ),
                ),
                (
                    "expense",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="finance.itemizedexpense",
                    ),
                ),
            ],
        ),
    ]
