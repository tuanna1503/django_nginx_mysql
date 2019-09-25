from django.conf import settings

def response_format(code=200, data=None):
    res_data = {}
    res_data['code'] = code
    res_data['data'] = data
    return res_data
