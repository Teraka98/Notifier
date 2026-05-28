import smtplib
import ssl

from loguru import logger


def send_message(port, smtp_server, sender_email, receiver_email, password):
    """
    Sends a message to the given SMTP server.
    :param port: PORT of the SMTP server
    :param smtp_server: SMTP server
    :param sender_email: email address of the sender
    :param receiver_email: email address of the receiver
    :param password: encryption password of the sender
    :return: None
    """
    logger.info(f'Sending message to {receiver_email}')
    message = """\
    Subject: Test Email

    Hi,
    Someone is here.
    """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(
            smtp_server,
            port,
            context=context,
    ) as server:
        server.login(sender_email, password)
        logger.info(f'SMTP server logged in as {sender_email}')
        # Send email here
        server.sendmail(
            sender_email,
            receiver_email,
            message,
        )
        logger.info(f'SMTP server sent message to {receiver_email}')
