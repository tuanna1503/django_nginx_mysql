from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('send_code/<mobile>', views.send_code, name='send_code'),
    path('login/<mobile>', views.login, name='login'),
]
