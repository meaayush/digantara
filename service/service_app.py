import django
import sys
import os


sys.path.append("F:/digantara")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "digantara.settings")

django.setup()


from flask import Flask
from utils.start_scheduler import start_scheduler
from flask_restful import Api
from service.controller.job_controller import JobController

app = Flask(__name__)
api = Api(app, '/digantara')

start_scheduler()

api.add_resource(JobController, '/jobs', '/jobs/<int:job_id>')

if __name__ == '__main__':
    app.run(debug=True, port=3001)
