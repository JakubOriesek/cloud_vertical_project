from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import job_get_api


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job_get_api, 'interval',seconds=20)
    scheduler.start()
    job_get_api()
    
    
