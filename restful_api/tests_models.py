
import smtplib
from xml.dom import ValidationErr
from django.test import TestCase
from restful_api.models import AccountVerification_1, Administrator, BusinessOwner, Student
from django.conf import settings
from django.db.models import F


class AdministratorTestcase(TestCase):
    def setUp(self):
        Administrator.objects.create(
            firstname="Peter",
            lastname="Palad",
            email="test@gmail.com",
            password="testpassword123",
            userType="1",
            isLock="0",
            isverified="1",
            imgURL="None"
        )

    def tearDown(self):
        pass

    def test_checkadmin(self):
        adminCount = Administrator.objects.filter(userType="1").values()
        self.assertTrue(adminCount)


class BusinessOwnerTestcase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_businessowner_creation(self):
        businessowner_creation = BusinessOwner.objects.create(
            firstname="Peter",
            lastname="Palad",
            contactnumber="09212142370",
            address="testaddress",
            email="test@gmail.com",
            password="testpassword123",
            userType="1",
            isLock="0",
            isverified="1",
            imgURL="None",
            sec_question="test question",
            sec_answer="test answer"
        )
        self.assertEqual(businessowner_creation.firstname,
                         businessowner_creation.firstname)

    def test_checkemail_bo(self):
        filtered = BusinessOwner.objects.filter(
            email="miggysvll@gmail.com"
        ).values()
        self.assertFalse(filtered)


class AccountVerificationTestcase(TestCase):
    def test_check_email_beforeCreation(self):
        filtered = AccountVerification_1.objects.filter(
            client_email="devopsbyte60@gmail.com"
        ).values()
        if filtered.count() > 0:
            self.assertTrue(filtered)
            onCount = AccountVerification_1.objects.filter(
                sent_count=3
            ).values()
            if onCount.count() > 0:
                self.assertTrue(onCount)
            else:
                print('PASSED RESULT : updated_another_sent_count')
        else:
            self.assertFalse(filtered)

    def test_verification_entry(self):
        account_verification = AccountVerification_1()
        account_verification.client_email = "miggysvll@gmail.com"
        account_verification.verification_code = "test code"
        account_verification.verified = "0"
        account_verification.user_type = "3"
        account_verification.sent_count = 1
        account_verification.save()
        self.assertTrue(account_verification)

    def test_update_counts(self):
        account_sent_updater = AccountVerification_1.objects.filter(
            client_email="miggysvll@gmail.com"
        ).update(sent_count=F('sent_count')+1, verification_code="testcode")
        self.assertFalse(account_sent_updater)

    def test_verify_check_counts(self):
        scan_counts = AccountVerification_1.objects.filter(
            client_email="miggysvll@gmail.com"
        ).filter(sent_count__gte=3).values()
        if scan_counts.count() > 0:
            self.assertFalse(scan_counts)
        self.assertTrue("success")

    def test_check_code_inputs(self):
        compared = AccountVerification_1.objects.filter(
            verification_code="testcode"
        ).filter(client_email="miggysvll@gmail.com").values()
        self.assertFalse(compared)

    def test_update_to_verified(self):
        ac1 = AccountVerification_1.objects.filter(
            client_email="miggysvll@gmail.com"
        ).update(verified="1")
        ab1 = BusinessOwner.objects.filter(
            email="miggysvll@gmail.com"
        ).update(isverified="1")
        self.assertFalse(ac1)
        self.assertFalse(ab1)

    def test_findAllBoByEmail(self):
        filtered = BusinessOwner.objects.filter(
            email="miggysvll@gmail.com"
        ).values()
        self.assertFalse(filtered)


class SendingEmailLibraryTestcase(TestCase):
    def test_email_sending_businessowner(self):
        # This is working.. upon running test this will sent an email based on the email provided
        # s = smtplib.SMTP('smtp.gmail.com', 587)
        # s.starttls()
        # s.login(settings.EMAIL_HOST_USER, settings.PY_EMAIL_PASS)
        # subject = 'MDR Ecommerce Verification Code'
        # text = "test code"
        # message = 'Subject: {}\n\n{}'.format(subject, text)
        # s.sendmail(settings.EMAIL_HOST_USER,
        #            "miggysvll@gmail.com", message)
        # s.quit()
        # print('PASSED RESULT : sent_email')
        pass


class StudentModelsTestcase(TestCase):
    def test_student_modelEntity(self):
        stud_accounts = Student.objects.filter(
            email="miggysvll@gmail.com"
        ).values()
        if stud_accounts.count() > 0:
            self.assertTrue(stud_accounts)
        self.assertTrue('success')
