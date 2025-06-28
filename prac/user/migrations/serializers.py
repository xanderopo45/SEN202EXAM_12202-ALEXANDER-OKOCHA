from rest_framework import serializers
from rest_framework.serializers import Serializer

from user.models import CompanyStaff


class Job:
    pass


class CompanyStaffSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.company_name', read_only=True)

    class Meta:
        model = CompanyStaff
        fields = [
            'id', 'company', 'company_name', 'title', 'description',
            'company', 'salary', 'job_type',
            'is_active', 'created_at', 'updated_at'
        ]
        extra_kwargs = {
            'company': {'write_only': True}
        }


class ApplicationSerializer(serializers.ModelSerializer):
    resume_details = Serializer(source='resume', read_only=True)
    job_title = serializers.CharField(source='job.title', read_only=True)
    company_name = serializers.CharField(source='job.company.company_name', read_only=True)

    class Meta:
        model = Application
        fields = [
            'id', 'job', 'job_title', 'company_name', 'resume', 'resume_details',
            'cover_letter', 'status', 'applied_at', 'updated_at'
        ]
        extra_kwargs = {
            'job': {'write_only': True},
            'resume': {'write_only': True}
        }
