from http.client import HTTPResponse

from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse

from config.settings import AUTH_USER_MODEL


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'auth_user'


class Profile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_img', null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'auth_user_profile'


