from orm.models.jobs import Job
from utils import scheduler
from utils.scheduler import schedule_job


def toggle_job(job_id):
    try:
        job = Job.objects.get(id=job_id)
        job.is_active = not job.is_active
        job.status = 'paused'
        job.save()
        if job.is_active:
            schedule_job(job)
            return {"message": "Job resumed"}, 200
        else:
            scheduler.remove_job(str(job.id))
            return {"message": "Job paused"}, 200
    except Job.DoesNotExist:
        return {"message": "Job not found"}, 404