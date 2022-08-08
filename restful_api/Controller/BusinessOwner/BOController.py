from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework import status
from restful_api.utils.helper import GeneralParams
from restful_api.utils.helper import GeneralHelper
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings
import smtplib


class BusinessOwnerController:
    @api_view(['GET'])
    def checkemail(request, email):
        if request.method == 'GET':
            GeneralHelper.Slug(
                'GET',
                'api/checking-email',
                email
            )
        return Response({"message": GeneralParams.params_result}, status=status.HTTP_200_OK)

    @api_view(['POST'])
    def businessowner_registration(request):
        if request.method == 'POST':
            collection = {
                "firstname": request.POST.get('firstname'),
                "lastname": request.POST.get('lastname'),
                "contactnumber": request.POST.get('contactnumber'),
                "address": request.POST.get('address'),
                "email": request.POST.get('email'),
                "password": request.POST.get('password'),
                "isverified": request.POST.get('isverified')
            }
            GeneralHelper.Slug(
                'POST',
                'api/business-owner-registration',
                collection
            )
            if GeneralParams.field_success_BO_registration == "success_bo_registration":
                return Response({"message": GeneralParams.field_success_BO_registration}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "something_wrong"}, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def business_verification(request, email, code):

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(settings.EMAIL_HOST_USER, settings.PY_EMAIL_PASS)
        subject = 'MDR Ecommerce Verification Code'
        text = code
        message = 'Subject: {}\n\n{}'.format(subject, text)
        s.sendmail(settings.EMAIL_HOST_USER,
                   email, message)
        s.quit()
        return Response(
            {
                "message": "success_sent"
            },
            status=status.HTTP_200_OK
        )



    @api_view(['GET'])
    def business_verify_email(request, email):
        if request.method == 'GET':
            GeneralHelper.Slug(
                'GET',
                'business-check-email-verification',
                email
            )
            return Response({"message" : GeneralParams.field_email_checker_str}, status=status.HTTP_200_OK)

    @api_view(['POST'])
    def business_verification_record(request):
        if request.method == 'POST':
            vc_collect = {
                "email": request.POST.get('email'),
                "code": request.POST.get('code')
            }
            GeneralHelper.Slug(
                'POST',
                'business-verification-dbentry',
                vc_collect
            )
            return Response(
                {
                    "message": GeneralParams.field_verification_bo
                },
                status=status.HTTP_200_OK
            )
    @api_view(['GET', 'PUT'])
    def business_update_with_sendemail(request, email, code):
        if request.method == 'PUT':
            BusinessOwnerController.send_email_helper(email, code)
            collective = {
                "email": email,
                "code": code
            }
            GeneralHelper.Slug(
                'PUT',
                'api/business-update-counts',
                collective
            )
            return Response({"message" : GeneralParams.field_update_counts}, status=status.HTTP_200_OK)

    @api_view(['GET'])
    def business_verification_checkcounts(request, email, code):
        if request.method == 'GET':
            GeneralHelper.Slug(
                'GET',
                'business-verification-check-counts',
                email
            )
            BusinessOwnerController.send_email_helper(email, code)
            collective = {
                "email": email,
                "code": code
            }
            GeneralHelper.Slug(
                'PUT',
                'api/business-update-counts',
                collective
            )
            return Response({"message": "success"}, status=status.HTTP_200_OK)
        return Response({"message": GeneralParams.field_check_counts.count()}, status=status.HTTP_200_OK)

    def send_email_helper(email, code):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(settings.EMAIL_HOST_USER, settings.PY_EMAIL_PASS)
        subject = 'MDR Ecommerce Verification Code'
        text = code
        message = 'Subject: {}\n\n{}'.format(subject, text)
        s.sendmail(settings.EMAIL_HOST_USER,
                   email, message)
        s.quit()
