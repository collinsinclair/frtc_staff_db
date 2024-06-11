from django.db import models
from core.models import StaffMember


class StatusType(models.Model):
    label = models.CharField(max_length=32)


class IssueTracking(models.Model):
    status = models.ForeignKey(
        StatusType, on_delete=models.SET_NULL, null=True, blank=True
    )
    assignee = models.ForeignKey(
        StaffMember, on_delete=models.SET_NULL, null=True, blank=True
    )
    notes = models.TextField(null=True, blank=True)


class WebsiteRequest(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    screenshot = models.ImageField(null=True, blank=True)
    issue_tracking = models.ForeignKey(
        IssueTracking, on_delete=models.SET_NULL, null=True, blank=True
    )
