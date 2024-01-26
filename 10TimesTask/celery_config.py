# celery_config.py
from celery import Celery
from app import create_app

flask_app = create_app()
celery = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
    include=['tasks']
)

celery.conf.update(flask_app.config)
