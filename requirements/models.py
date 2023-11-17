# models.py
from django.db import models

class JobRequirement(models.Model):
    MANAGEMENT_LEVEL_JOBS = [
        ('manager', 'Manager'),
        ('supervisor', 'Supervisor'),
        ('director', 'Director'),
        # Add other management-level jobs as needed
    ]

    job_title = models.CharField(max_length=100, choices=MANAGEMENT_LEVEL_JOBS)
    skill_requirement = models.TextField()
    experience_requirement = models.IntegerField()
    # Add other fields as needed

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    job_applied_for = models.ForeignKey(JobRequirement, on_delete=models.CASCADE)
    # Add other candidate-related fields as needed

class InterviewAnswer(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='interview_answers')
    answer_text = models.TextField()
    # Add other fields as needed
