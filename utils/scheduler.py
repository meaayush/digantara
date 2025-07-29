from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime

bg_scheduler = BackgroundScheduler()

def dummy_job(job):
    job_id = job.id
    print(f"Running dummy job {job_id} at {datetime.now()}")
    job.last_run = datetime.now()
    job.next_run = bg_scheduler.get_job(str(job_id)).next_run_time
    job.save()

def schedule_job(job):
    if not job.is_active:
        print(f"job {job.id} is not active")
        return

    trigger = CronTrigger(
        **{k: v for k, v in job.cron_dict().items() if v},
        end_date=job.end_time
    )
    bg_scheduler.add_job(lambda: dummy_job(job), trigger, id=str(job.id))
    aps_job = bg_scheduler.get_job(str(job.id))
    if aps_job:
        job.next_run = aps_job.next_run_time
        job.save()


