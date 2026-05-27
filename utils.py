import smtplib
import ssl

import qrcode
from loguru import logger


def generate_qr_code(link, fill_color='black', back_color='white'):
    """
    Generates a QR code from the given link and displays it in the notebook.

    :param link: The URL or text to encode in the QR code.
    :param fill_color: The color of the QR code (default is 'black').
    :param back_color: The background color of the QR code (default is 'white').
    """
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code (1 is the smallest, 40 is the largest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code
        border=4,  # Border size around the QR code
    )

    # Add data to the QR code
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    logger.info(f'QR code generated: {link}')
    img.save('static/qrcode.png')
    logger.success('QR code generated in static/qrcode.png')


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
