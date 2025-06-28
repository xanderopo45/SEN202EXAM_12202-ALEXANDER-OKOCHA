from typing import Any

from django.db import models

class CompanyStaff(models.Model):
    company = models.ForeignKey( on_delete=models.CASCADE, related_name='company staffs')
    title = models.CharField(max_length=200)
    description = models.TextField()
    department = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    job_type = models.CharField(max_length=50)  # Full-time, Part-time, Contract, etc.
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.company.company_name}"

    class Application(models.Model):

        cover_letter = models.TextField(blank=True, null=True)
        status = models.CharField(max_length=50, default='applied')  # applied, reviewed, rejected, etc.
        applied_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        class Meta:
            unique_together = ('job', 'resume')  # Prevent duplicate applications

        def __init__(self, *args: Any, **kwargs: Any):
            super().__init__(args, kwargs)
            self.job = None
            self.user = None

        def __str__(self):
            return f"Application for {self.job.title} by {self.user.email}"


class User:
    DoesNotExist = None
    objects = None