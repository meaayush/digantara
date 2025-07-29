from flask_restful import Resource
from flask import request
from orm.models.jobs import Job
from service.views.job_views import all_jobs, single_job
from utils import scheduler

class JobController(Resource):
    def get(self, job_id=None):
        if job_id is not None:
            try:
                job = Job.objects.get(id=job_id)
            except Job.DoesNotExist:
                return {"message": "Job not found"}, 404
            return single_job(job), 200
        jobs = Job.objects.all()
        return all_jobs(jobs), 200

    def post(self):
        data = request.get_json()
        job = Job.create_and_schedule(data)
        return {
            "id": job.id, 
            "message": "Job created"
        }, 201
    
    def put(self, job_id):
        try:
            job = Job.objects.get(id=job_id)
            job.is_active = not job.is_active
            job.status = 'scheduled' if job.is_active else 'paused'
            job.save()
            if job.is_active:
                scheduler.schedule_job(job)
                return {"message": "Job resumed"}, 200
            else:
                scheduler.remove_job(str(job.id))
                return {"message": "Job paused"}, 200
        except Job.DoesNotExist:
            return {"message": "Job not found"}, 404
    
    def delete(self, job_id):
        if job_id is None:
            return {"message": "Job Id missing"}, 404
        
        try:
            job = Job.objects.get(id=job_id)
            scheduler.remove_job(str(job.id))
            job.delete()
            return {"message": "Job deleted"}, 200
        except Job.DoesNotExist:
            return {"message": "Job not found"}, 404