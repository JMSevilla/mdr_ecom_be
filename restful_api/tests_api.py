from django.test import TestCase


class BusinessOwnerSerializerTestCase(TestCase):
    def test_business_owner_creation_api(self):
        payload = {
            "firstname": "bryan",
            "lastname": "palad",
            "contactnumber": "09212142370",
            "address": "test address",
            "email": "miggysvll@gmail.com",
            "password": "5418873",
            "isverified": "1",
            "sec_question": "test security questions",
            "sec_answer": "test security answer"
        }
        response = self.client.post(
            '/api/businessowner/registration/', payload
        )
        self.assertEqual(response.status_code, 200)
        print("passed: business_owner_created", response.status_code)

    # Also working same with test model send email
    # def test_business_send_email_api(self):
    #     response = self.client.get(
    #         '/api/business-checkemail/miggysvll@gmail.com/testcode/')
    #     self.assertEqual(response.status_code, 200)
    #     print("business_sent_email", response.status_code)

    def test_business_checkEmailVerification_api(self):
        response = self.client.get(
            '/api/check-email-verification/miggysvll@gmail.com/'
        )
        self.assertEqual(response.status_code, 200)
        print('passed: check_email_api', response.status_code)

    def test_business_verification_record_api(self):
        payload = {
            "email": "miggysvll@gmail.com",
            "code": "testcode123"
        }
        response = self.client.post(
            '/api/verification-entry', payload
        )
        self.assertEqual(response.status_code, 200)
        print('passed: verify_record', response.status_code)

    def test_business_update_with_sendemail_api(self):
        response = self.client.put(
            '/api/business-update-with-send/miggysvll@gmail.com/testcode123/'
        )
        self.assertEqual(response.status_code, 200)
        print('passed: update_with_sendemail', response.status_code)
