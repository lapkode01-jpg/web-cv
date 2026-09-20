import logging
from celery import Celery
import os
from dotenv import load_dotenv
from celery.signals import setup_logging
load_dotenv()

@setup_logging.connect
def config_logger(*args, **kwargs):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler('app.log', encoding='utf-8')
        ]
    )


rabbit_user = os.getenv('RABBITMQ_DEFAULT_USER')
rabbit_password = os.getenv('RABBITMQ_DEFAULT_PASS')

celery_app = Celery('main_process',
                    broker=f'amqp://{rabbit_user}:{rabbit_password}@rabbitmq:5672/email_broker',
                    include=['worker']
)




