# coding: utf-8
from __future__ import unicode_literals
from django.db import models


class FbUser(models.Model):
    username = models.CharField(max_length=128)
    facebookId = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=256)
    gender = models.CharField(max_length=8)


class FbUserLog(models.Model):
    ACTIONS_CHOICES = (
        ('created', 'New register'),
        ('updated', 'Register Updated'),
        ('deleted', 'Register deleted'),
        ('error', 'API error')
    )
    action = models.CharField(max_length=8, choices=ACTIONS_CHOICES)
    facebookId = models.CharField(max_length=32)
    date = models.DateTimeField(auto_now_add=True)
    error_code = models.CharField(max_length=32, null=True, blank=True)

    def set_user(self, user):
        self.facebookId = user.facebookId
