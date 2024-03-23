from django.forms import (
    BooleanField,
    CharField,
    ChoiceField,
    EmailField,
    Field,
    Form,
    ModelMultipleChoiceField,
    ValidationError,
)

from allauth.headless.restkit.response import ErrorResponse


__all__ = [
    "Field",
    "CharField",
    "ChoiceField",
    "ValidationError",
    "EmailField",
    "BooleanField",
    "ModelMultipleChoiceField",
]


class Input(Form):
    @property
    def error_dict(self):
        ret = {}
        for field, error_list in self.errors.items():
            ret[field] = error_list.get_json_data()
        return ret

    def respond_error(self):
        return ErrorResponse(self.error_dict)
