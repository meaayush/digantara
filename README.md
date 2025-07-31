Project Setup:
  - Clone the repo
  - Create and activate the virtual environment
      python3 -m venv venv
      source venv/bin/activate
  - Install dependencies
      pip install -r requirements.txt
  - I have already hardcoded the postgres connection string so no need to setup a database and run migrations.
  - You can run the service using two commands:
      1. python service/service_app.py
      2. gunicorn service.service_app:app -c gunicorn_config.py
    
