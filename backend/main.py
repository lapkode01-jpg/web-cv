from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from config import celery_app
from schema import EmailSchema
from dotenv import load_dotenv
import logging
load_dotenv()
app = FastAPI()


logger = logging.getLogger(__name__)

app.add_middleware(
    CORSMiddleware,
    allow_methods=['POST'],
    allow_headers=['*'],
    allow_credentials=True,
    allow_origins=['*']
)

@app.post('/api/send-email/')
async def send_mail(email_body: EmailSchema):
    try:
        celery_app.send_task(
            'worker.send_email2host',
            args=[email_body.username, email_body.text],
            queue='queue.send_email',
        )
        celery_app.send_task(
            'worker.send_email2user',
            args=[email_body.username, email_body.email],
            queue='queue.send_email',
        )
        logger.info(f'[SUCCESS]:main: {email_body.email} send')
        return {"status": "success"}
    except Exception as e:
        logger.error(f'[ERROR]:main: {e}', exc_info=e)
        return {"status": "error"}


















































