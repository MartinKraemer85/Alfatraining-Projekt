import smtplib
from decouple import config


def test_mail(to='m.kraemer85@web.de'):
    """
    Sends an email to a specifici mail adress

    :param to: Receiver
    :return: None
    """
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(config('FROM_ADDR'), config('MAIL_KEY'))
        connection.sendmail(from_addr=config('FROM_ADDR'), to_addrs=to,
                            msg="subject:hi \n\n this is my message")

