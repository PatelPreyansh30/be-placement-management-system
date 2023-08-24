from rest_framework.views import exception_handler
from rest_framework.response import Response


def flatten_nested_errors(nested_errors):
    flat_errors = []
    for field_errors in nested_errors.values():
        flat_errors.extend(field_errors)
    return flat_errors


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(response.data, dict):
            if response.data.get('detail'):
                custom_response_data = {
                    'detail': [response.data.get('detail')],
                }
            else:
                custom_response_data = {
                    'detail': flatten_nested_errors(response.data),
                }
            response.data = custom_response_data

    return response
