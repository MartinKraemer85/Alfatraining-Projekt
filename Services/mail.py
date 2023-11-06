import smtplib
from decouple import config


def test_mail(receiver='m.kraemer85@web.de') -> None:
    """
    Sends an email to a specific mail address

    :param receiver: Receiver
    :return: None
    """
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(config('FROM_ADDR'), config('MAIL_KEY'))
        connection.sendmail(from_addr=config('FROM_ADDR'), to_addrs=receiver,
                            msg="subject:Miau \n\n this is my message")

