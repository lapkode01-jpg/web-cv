from email.message import EmailMessage
import smtplib
import logging
import os
from config import celery_app
from dotenv import load_dotenv
from html_plain import get_beauti_html

load_dotenv()

logger = logging.getLogger(__name__)

HOST_EMAIL = os.getenv('SEND_TO')
HOST_PASSWORD = os.getenv('APP_PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')



def send_message(to_email: str, body_text: str, subject: str):
    message = EmailMessage()
    message['To'] = to_email
    message['From'] = HOST_EMAIL
    message['Subject'] = subject

    message.set_content(body_text, subtype='html')
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(HOST_EMAIL, HOST_PASSWORD)
                server.send_message(message)
    except Exception as e:
        logger.error(f'[ERROR]:worker: {e}', exc_info=True)
    return True



@celery_app.task(name='worker.send_email2host', queue='queue.send_email')
def send_email_task2host(username: str, body_text: str):
    logger.info(
        f'[TASK START] send_email2host: '
        f'username={username!r}, body={body_text!r}'
    )

    to_email = HOST_EMAIL
    subject = f'Job offer from {username}'
    if send_message(to_email, body_text, subject):
        return True
    logger.error(f'[ERROR] - tasks.send_email - dont send')
    raise RuntimeError("Message dont send")



@celery_app.task(name='worker.send_email2user', queue='queue.send_email')
def send_email_task2user(username: str, to_email: str):
    body_text = get_beauti_html(username)
    subject = f'From Andrei Lapko to {username}'

    if send_message(to_email, body_text, subject):
        return True
    logger.error(f'[ERROR] - tasks.send_email - dont send')
    raise RuntimeError("Message dont send")














































