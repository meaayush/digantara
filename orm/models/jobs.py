from django.db import models
from datetime import datetime
from utils.scheduler import schedule_job

class Job(models.Model):
    name = models.CharField(max_length=100)
    schedule_minute = models.CharField(max_length=10, blank=True, null=True)
    schedule_hour = models.CharField(max_length=10, blank=True, null=True)
    schedule_day = models.CharField(max_length=10, blank=True, null=True)
    schedule_month = models.CharField(max_length=10, blank=True, null=True)
    schedule_day_of_week = models.CharField(max_length=10, blank=True, null=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    last_run = models.DateTimeField(null=True, blank=True)
    next_run = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='scheduled')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def cron_dict(self):
        return {
            'minute': self.schedule_minute,
            'hour': self.schedule_hour,
            'day': self.schedule_day,
            'month': self.schedule_month,
            'day_of_week': self.schedule_day_of_week
        }

    @classmethod
    def create_and_schedule(cls, data):
        job = cls.objects.create(
            name=data['name'],
            schedule_minute=data['schedule'].get('minute'),
            schedule_hour=data['schedule'].get('hour'),
            schedule_day=data['schedule'].get('day'),
            schedule_month=data['schedule'].get('month'),
            schedule_day_of_week=data['schedule'].get('day_of_week'),
            end_time=data.get('end_time'),  
            is_active=data.get('is_active', True)
        )
        schedule_job(job)
        return job