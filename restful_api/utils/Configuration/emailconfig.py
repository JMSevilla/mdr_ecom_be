import smtplib
from restful_api.models import BusinessOwner, Student
from django.conf import settings


class EmailConfigResponse:
    email_message = ''
    student_email_message = ''


class EmailConfig:
    def config_checkemail(params):
        bo_accounts = BusinessOwner.objects.filter(
            email=params
        ).values()
        if bo_accounts.count() > 0:
            EmailConfigResponse.email_message = "exist"
            return EmailConfigResponse.email_message
        else:
            EmailConfigResponse.email_message = "not_exist"
            return EmailConfigResponse.email_message

    def student_config_checkemail(params):
        stud_accounts = Student.objects.filter(
            email=params
        ).values()
        if stud_accounts.count() > 0:
            EmailConfigResponse.student_email_message = "exist"
            return EmailConfigResponse.student_email_message
        else:
            EmailConfigResponse.student_email_message = "not_exist"
            return EmailConfigResponse.student_email_message

    def sendEmailHelper(email, code):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(settings.EMAIL_HOST_USER, settings.PY_EMAIL_PASS)
        subject = 'MDR Ecommerce Verification Code'
        text = code
        message = 'Subject: {}\n\n{}'.format(subject, text)
        s.sendmail(settings.EMAIL_HOST_USER,
                   email, message)
        s.quit()
