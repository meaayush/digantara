fmt = "%Y-%m-%d %H:%M:%S"
def all_jobs(jobs):
    return [
        {
            "id": job.id,
            "name": job.name,
            "last_run": job.last_run.strftime(fmt) if job.last_run else None,
            "next_run": job.next_run.strftime(fmt) if job.next_run else None,
            "end_time": job.end_time.strftime(fmt) if job.end_time else None,
            "is_active": job.is_active,
            "status": job.status
        }
        for job in jobs
    ]

def single_job(job):
    return {
        "id": job.id,
        "name": job.name,
        "schedule": {
            "minute": job.schedule_minute,
            "hour": job.schedule_hour,
            "day": job.schedule_day,
            "month": job.schedule_month,
            "day_of_week": job.schedule_day_of_week,
        },
        "last_run": job.last_run.strftime(fmt) if job.last_run else None,
        "next_run": job.next_run.strftime(fmt) if job.next_run else None,
        "end_time": job.end_time.strftime(fmt) if job.end_time else None,
        "is_active": job.is_active,
        "created_at": job.created_at.strftime(fmt) if job.end_time else None,
        "status": job.status
    }