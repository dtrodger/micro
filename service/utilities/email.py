from flask import current_app
from flask_mail import Message

from project.configuration.extensions import mail_api


def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=current_app.config['MAIL_DEFAULT_SENDER']
    )
    mail_api.send(msg)
