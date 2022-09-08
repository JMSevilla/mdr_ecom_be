from restful_api.models import BusinessOwner

class EmailConfigResponse:
    email_message = ''

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
        