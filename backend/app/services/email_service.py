# backend/app/services/email_service.py

from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
from ..config import settings

conf = ConnectionConfig(
    MAIL_USERNAME = "your-email@example.com",
    MAIL_PASSWORD = "your-email-password",
    MAIL_FROM = settings.EMAIL_FROM,
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.example.com",
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

async def send_email(email: EmailStr, subject: str, body: str):
    message = MessageSchema(
        subject=subject,
        recipients=[email],
        body=body,
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)
