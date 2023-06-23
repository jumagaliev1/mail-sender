import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

config = {
    'SMTP_HOST': '',
    'SMTP_PORT': '',
    'SMTP_SENDER':'',
    'SMTP_PASSWORD':'',
    'SMTP_NAME':'',
}

def init_config(self, config):
    self.config = config



def smtp(title: str, content: str, email_getter: str) -> None:
    smtp_server = smtplib.SMTP(config["SMTP_HOST"], config["SMTP_PORT"])

    smtp_server.starttls()

    smtp_server.login(config["SMTP_SENDER"], config["SMTP_PASSWORD"])

    message = MIMEText(content, "plain", "utf-8")
    
    message["From"] = formataddr(
        (
            Header(config["SMTP_NAME"], "utf-8").encode(),
            config["SMTP_SENDER"],
        )
    )
    message["Subject"] = title

    smtp_server.sendmail(config["SMTP_SENDER"], email_getter, message.as_bytes())
    smtp_server.close()
    print("finish...")