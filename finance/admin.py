from django.contrib import admin
from .models import *

models = [ExpenseCategory, ItemizedExpense, ExpenseStatus, ExpenseReview]
for model in models:
    admin.site.register(model)
