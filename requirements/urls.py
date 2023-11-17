from django.urls import path
from .views import requirement_form, job_application

urlpatterns = [
    path('job/<int:job_id>/', job_application, name='job_application'),
    path('requirement_form/', requirement_form, name='requirement_form'),
]
