# Generated by Django 3.2 on 2023-11-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requirements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequirement',
            name='job_title',
            field=models.CharField(choices=[('manager', 'Manager'), ('supervisor', 'Supervisor'), ('director', 'Director')], max_length=100),
        ),
    ]
