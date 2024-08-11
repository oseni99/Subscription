import base64

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


# use the password reset token generator to generate tokens for email verify
class UserVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp: int):
        user_id = six.text_type(user.pk)
        ts = six.text_type(timestamp)
        is_active = six.text_type(user.is_active)
        return f"{user_id}{ts}{is_active}"


user_tokenize_generator = UserVerificationTokenGenerator()


def urlsafe_base64_encode(data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    encoded_bytes = base64.urlsafe_b64encode(data)
    return encoded_bytes.decode("utf-8")


def urlsafe_base64_decode(data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    encoded_bytes = base64.urlsafe_b64decode(data)
    return encoded_bytes.decode("utf-8")
