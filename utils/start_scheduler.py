from orm.models.jobs import Job
from utils.scheduler import bg_scheduler, schedule_job


def start_scheduler():
    bg_scheduler.start()
    for job in Job.objects.all():
        schedule_job(job)