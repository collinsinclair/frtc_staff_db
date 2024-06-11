from django.contrib import admin
from .models import *

models = [
    Location,
    ProductionType,
    Responsibility,
    Role,
    PhoneNumber,
    Email,
    StaffMember,
    Production,
    Committee,
]
for model in models:
    admin.site.register(model)
