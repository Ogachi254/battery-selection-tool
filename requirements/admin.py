# admin.py
from django.contrib import admin
from .models import JobRequirement, Candidate, InterviewAnswer

@admin.register(JobRequirement)
class JobRequirementAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'skill_requirement', 'experience_requirement')

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_applied_for')

@admin.register(InterviewAnswer)
class InterviewAnswerAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'answer_text')
