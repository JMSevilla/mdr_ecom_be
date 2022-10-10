from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings


class MDRHasher:
    def encrypt(__val__):
        try:
            pas = str(__val__)
            cipher_val = Fernet(settings.ENCRYPT_KEY)
            encrypt_val = cipher_val.encrypt(pas.encode('ascii'))
            encrypt_val = base64.urlsafe_b64encode(encrypt_val).decode('ascii')
            return encrypt_val
        except Exception as e:
            logging.Logger("error_logger").error(traceback.format_exc())
            return None

    def decrypt(__val__):
        try:
            pas = base64.urlsafe_b64decode(__val__)
            cipher_pass = Fernet(settings.ENCRYPT_KEY)
            decod_pass = cipher_pass.decrypt(pas).decode("ascii")
            return decod_pass
        except Exception as e:
            logging.getLogger("error_logger").error(traceback.format_exc())
            return None
