import random, jwt

from django.shortcuts import render
from django.http import JsonResponse

from spa.services.utils import response_format
from users.models import User, Otp


def send_code(request, mobile):
    code = random.randrange(1000, 9999)
    # find or create user
    auth_token = jwt.encode({'code': code}, 'SECRET_KEY_SPA_APP', algorithm='HS256')
    user, created = User.objects.get_or_create(mobile=mobile, defaults={'auth_token': auth_token},)
    # save otp
    otp = Otp(mobile=mobile, code=code, user=user)
    otp.save()

    response = response_format(data={
        'otp_code': code
    })
    return JsonResponse(response, safe=False)


def login(request, mobile):
    otp_code = request.GET.get('otp_code')
    # find user from otp

    response = response_format(data=user)
    return JsonResponse(response, safe=False)