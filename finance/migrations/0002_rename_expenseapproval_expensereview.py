# Generated by Django 5.0.6 on 2024-06-11 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_staffmember_reports_to"),
        ("finance", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ExpenseApproval",
            new_name="ExpenseReview",
        ),
    ]
