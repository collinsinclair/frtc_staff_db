from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"


class ProductionType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Production Type"
        verbose_name_plural = "Production Types"


class Responsibility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Responsibility"
        verbose_name_plural = "Responsibilities"


class Role(models.Model):
    name = models.CharField(max_length=100)
    responsibilities = models.ManyToManyField(
        Responsibility,
        blank=True,
        help_text="Choose any and only responsibilities that are inseparable from this role.",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"


class PhoneNumber(models.Model):
    phone_number = models.IntegerField(unique=True)
    note = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="e.g. 'Collin Sinclair Cell' or 'PPA Main'",
    )

    def __str__(self):
        return f"{self.phone_number}"

    class Meta:
        verbose_name = "Phone Number"
        verbose_name_plural = "Phone Numbers"


class Email(models.Model):
    email = models.EmailField(unique=True)
    note = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"


class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(
        max_length=32, blank=True, help_text="Leave blank if User is selected above."
    )
    last_name = models.CharField(
        max_length=32, blank=True, help_text="Leave blank if User is selected above."
    )
    primary_phone_number = models.ForeignKey(
        PhoneNumber,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="person_primary_phone",
    )
    other_phone_numbers = models.ManyToManyField(
        PhoneNumber, blank=True, related_name="person_other_phones"
    )
    primary_email_address = models.ForeignKey(
        Email,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="person_primary_email",
    )
    other_email_addresses = models.ManyToManyField(
        Email, blank=True, related_name="person_other_emails"
    )

    def save(self, *args, **kwargs):
        if self.user:
            if not self.first_name:
                self.first_name = self.user.first_name
            if not self.last_name:
                self.last_name = self.user.last_name
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        abstract = True
        verbose_name = "Person"
        verbose_name_plural = "People"


class StaffMember(Person):
    roles = models.ManyToManyField(Role, blank=True)
    responsibilities = models.ManyToManyField(Responsibility, blank=True)
    reports_to = models.ForeignKey(
        "StaffMember", null=True, blank=True, on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = "Staff Member"
        verbose_name_plural = "Staff Members"


class Production(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(help_text="The date of the first rehearsal, usually.")
    opening_date = models.DateField(
        help_text="The date of the first performance, usually."
    )
    closing_date = models.DateField(
        null=True, blank=True, help_text="The date of the last performance, usually."
    )
    staff = models.ManyToManyField(StaffMember, blank=True)
    locations = models.ManyToManyField(Location, blank=True)
    classification = models.ForeignKey(ProductionType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Production"
        verbose_name_plural = "Productions"


class Committee(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(StaffMember)

    class Meta:
        verbose_name = "Committee"
        verbose_name_plural = "Committees"
