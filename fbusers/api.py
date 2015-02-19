# coding: utf-8
from __future__ import unicode_literals
import requests


def get_fb_user(id):
    url = 'https://graph.facebook.com/{id}'.format(id=id)
    return requests.get(url)
