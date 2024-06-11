import datetime

from django.db import models

from core.models import StaffMember


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Expense Categories"


class ItemizedExpense(models.Model):
    vendor = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
    date_of_transaction = models.DateField()
    category = models.ForeignKey(
        ExpenseCategory, on_delete=models.PROTECT, null=True, blank=True
    )
    value = models.DecimalField(decimal_places=2, max_digits=10)
    note = models.TextField(null=True, blank=True)
    receipt = models.ImageField()
    purchaser = models.ForeignKey(StaffMember, on_delete=models.PROTECT)


class ExpenseStatus(models.Model):
    status = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "Expense Statuses"


class ExpenseReview(models.Model):
    expense = models.ForeignKey(ItemizedExpense, on_delete=models.PROTECT)
    status = models.ForeignKey(ExpenseStatus, on_delete=models.PROTECT)
    reviewed_by = models.ForeignKey(StaffMember, on_delete=models.PROTECT)
    review_date = models.DateField(default=datetime.date.today)
