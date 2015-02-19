# coding: utf-8
from __future__ import unicode_literals
from rest_framework import serializers
from fbusers.models import FbUser


class FbUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FbUser
        fields = ('username', 'facebookId', 'name', 'gender')
