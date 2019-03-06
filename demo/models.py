
from schematics.models import Model
from schematics import types

from schematics.exceptions import ValidationError


class EmailType(types.BaseType):
    MESSAGES = {
        'missing_at': 'Email addresses must contain \'@\''
    }

    def validate_at(self, value):
        if '@' not in value:
            raise ValidationError(self.MESSAGES['missing_at'])


class User(Model):
    id = types.UUIDType(required=False)
    name = types.StringType(required=False)
    email = EmailType(required=True)
    created_at = types.DateTimeType(required=False)
    updated_at = types.DateTimeType(required=False)
    deleted_at = types.DateTimeType(required=False)
    profile = types.DictType(types.StringType, default={}, required=False)
