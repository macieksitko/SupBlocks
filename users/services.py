from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from eth_utils import is_address


def validate_address(value):
    if not is_address(value):
        raise ValidationError(
            _('%(value)s is not a valid account address'),
            params={'value': value},
        )