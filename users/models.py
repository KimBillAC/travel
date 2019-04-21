from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserProfile(AbstractUser):

    GENDER_CHOICE = (
        ('male', u'男'),
        ('female', u'女')
    )

    name = models.CharField('姓名', max_length=20, null=True, blank=True)
    gender = models.CharField('性别',max_length=10, choices=GENDER_CHOICE, default='male')
    mobile = models.CharField('电话', max_length=11, null=True, blank=True)
    birthday = models.DateField('出生日期', null=True, blank=True)
    email = models.CharField('邮箱', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.name


class VerifyCode(models.Model):
    pass