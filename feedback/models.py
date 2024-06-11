from django.db import models
from core.models import StaffMember


class StatusType(models.Model):
    label = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Status Type"
        verbose_name_plural = "Status Types"


class IssueTracking(models.Model):
    status = models.ForeignKey(
        StatusType, on_delete=models.SET_NULL, null=True, blank=True
    )
    assignee = models.ForeignKey(
        StaffMember, on_delete=models.SET_NULL, null=True, blank=True
    )
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Issue Tracking"
        verbose_name_plural = "Issue Trackings"


class WebsiteRequest(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    screenshot = models.ImageField(null=True, blank=True)
    issue_tracking = models.ForeignKey(
        IssueTracking, on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = "Website Request"
        verbose_name_plural = "Website Requests"
