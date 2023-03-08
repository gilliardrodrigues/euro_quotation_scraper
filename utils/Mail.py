import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

__all__ = [
    'send'
]


class Mail:

    def __init__(self, sender, password):
        # Configuration:
        self.host = 'smtp.gmail.com'
        self.port = 587
        self.sender = sender
        self.password = password
        self.server = smtplib.SMTP(self.host, self.port)
        # Logging into the server:
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.sender, self.password)

    def send(self, subject, message, receiver):
        """
        Send the e-mail message.
        Parameters
        ----------
        subject : str
            The subject of the e-mail.
        message : str
            Text message of the e-mail.
        receiver : str
            E-mail address of the receiver.
        Returns
        ----------
        """
        # Creating the message:
        email_msg = MIMEMultipart()
        email_msg['From'] = self.sender
        email_msg['To'] = receiver
        email_msg['Subject'] = subject
        email_msg.attach(MIMEText(message, 'plain'))
        # Sending the message:
        self.server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        print('E-mail enviado!')
        self.server.quit()
