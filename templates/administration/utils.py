from django.core.mail import send_mail
from django.conf import settings


def send_member_email(member, subject, message):
    """
    Sends an email to the specified member.
    :param member: Member object (assumes it has an 'email' attribute)
    :param subject: Subject of the email
    :param message: Body of the email
    """
    recipient_list = [member.email]
    from_email = settings.EMAIL_HOST_USER

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
    )
