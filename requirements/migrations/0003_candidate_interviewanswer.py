# Generated by Django 3.2 on 2023-11-17 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requirements', '0002_alter_jobrequirement_job_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('job_applied_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requirements.jobrequirement')),
            ],
        ),
        migrations.CreateModel(
            name='InterviewAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interview_answers', to='requirements.candidate')),
            ],
        ),
    ]