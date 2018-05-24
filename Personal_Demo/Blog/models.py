from django.db import models
from django.contrib.admin.widgets import *

# Create your models here.


class UserInfo(models.Model):
    account = models.CharField('account', max_length=60)
    passwd = models.CharField('passwd', max_length=100)

    def __str__(self):
        return self.account
