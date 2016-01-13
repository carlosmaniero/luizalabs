# coding: utf-8
from __future__ import unicode_literals
import facebook
from django.conf import settings


def get_fb_user(id):
    graph = facebook.GraphAPI(access_token=settings.ACCESS_TOKEN)
    return graph.get_object(id)
