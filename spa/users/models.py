from django.db import models

class User(models.Model):
    mobile = models.CharField(max_length=30)
    auth_token = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'app_users'


class Otp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=30)
    code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'app_otps'