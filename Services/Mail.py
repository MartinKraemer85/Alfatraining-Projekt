import smtplib
from decouple import config


def mail(first_name: str, last_name: str, mail_address: str, subject: str, issue: str) -> None:
    """
    Sends an email to a specific mail address

    :param first_name: first name of sender
    :param last_name: last name of sender
    :param mail_address: mail address of sender
    :param subject: mail subject
    :param issue: issue
    :return: None
    """
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(config('FROM_ADDR'), config('MAIL_KEY'))
        connection.sendmail(from_addr=config('FROM_ADDR'), to_addrs=config('TO_ADDR'),
                            msg=f"""subject: {subject} \n\n 
                                    first_name: {first_name} 
                                    last_name: {last_name} 
                                    mail_address: {mail_address}
                                    issue: {issue}""")
