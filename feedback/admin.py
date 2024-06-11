from django.contrib import admin
from .models import *

models = [StatusType, IssueTracking, WebsiteRequest]
for model in models:
    admin.site.register(model)
