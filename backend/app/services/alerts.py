import smtplib
from email.message import EmailMessage


class AlertDispatcher:
    def send_email(self, smtp_host: str, sender: str, recipient: str, subject: str, body: str) -> None:
        msg = EmailMessage()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.set_content(body)

        with smtplib.SMTP(smtp_host) as server:
            server.send_message(msg)
