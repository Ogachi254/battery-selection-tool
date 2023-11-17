# forms.py
from django import forms
from .models import JobRequirement

class JobRequirementForm(forms.ModelForm):
    class Meta:
        model = JobRequirement
        fields = ['job_title', 'skill_requirement', 'experience_requirement']
        
        widgets = {
            'skill_requirement': forms.Textarea(attrs={'rows': 4}),
        }