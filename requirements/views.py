# views.py
from django.shortcuts import render, redirect
from .forms import JobRequirementForm
from .models import InterviewAnswer, JobRequirement, Candidate
from .utils.recruitment_system import RecruitmentSystem

def job_application(request, job_id):
    job = JobRequirement.objects.get(pk=job_id)
    interview_questions = RecruitmentSystem.interview_questions()

    if request.method == 'POST':
        candidate_name = request.POST.get('candidate_name')
        candidate_answers = [request.POST.get(f'answer_{i+1}') for i in range(len(interview_questions))]

        candidate = Candidate.objects.create(name=candidate_name, job_applied_for=job)
        for answer_text in candidate_answers:
            InterviewAnswer.objects.create(candidate=candidate, answer_text=answer_text)

        return render(request, 'requirements/thank_you.html', {'candidate': candidate})

    context = {
        'job': job,
        'interview_questions': interview_questions,
    }

    return render(request, 'requirements/job_application.html', context)


def requirement_form(request):
    if request.method == 'POST':
        form = JobRequirementForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'requirements/thank_you.html')
    else:
        form = JobRequirementForm()

    return render(request, 'requirements/requirement_form.html', {'form': form})
