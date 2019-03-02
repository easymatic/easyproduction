from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError, APIException

UNHANDLED_ERROR = 'Unhandled error'


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if not isinstance(exc, APIException):
        response.data = {
            'code': response.status_text,
            'message': response.data.get('detail', UNHANDLED_ERROR),
            'misc': '',
        }
        return response
    full_detail = exc.get_full_details()
    if isinstance(full_detail, dict) and isinstance(exc, ValidationError):
            data = response.data.copy()
            response.data = {
                'code': 'validation_error',
                'message': 'ValidationError, check misc attribute',
                'misc': getattr(exc, 'misc', data),
            }
            return response
    if isinstance(full_detail, dict):
        detail = full_detail
    elif isinstance(full_detail, (tuple, list)):
        detail = full_detail[0]
    response.data = {
        'code': detail.get('code', exc.default_code),
        'message': detail.get('message', 'Unhandled error'),
        'misc': getattr(exc, 'misc', ''),
    }
    return response
