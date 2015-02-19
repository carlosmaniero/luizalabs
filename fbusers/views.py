# coding: utf-8
from __future__ import unicode_literals
from fbusers.models import FbUser, FbUserLog
from fbusers.serializers import FbUserSerializer
from fbusers.api import get_fb_user
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class FbUserList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):

    serializer_class = FbUserSerializer
    paginate_by = 10
    paginate_by_param = 'limit'
    max_paginate_by = 100

    def get_queryset(self):
        return FbUser.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        facebookId = self.request.data.get('facebookId', None)

        if facebookId is None or facebookId is '':
            return Response({'error': 'facebookId field is required'}, status=status.HTTP_400_BAD_REQUEST)

        request = get_fb_user(facebookId)

        log = FbUserLog()
        log.facebookId = facebookId

        if request.status_code == 200:
            json = request.json()
            json['name'] = json['first_name'] + ' ' + json['last_name']
            json['facebookId'] = json['id']
            serializer = FbUserSerializer(data=json)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            log.action = 'created'
            log.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        log.action = 'error'
        log.error_code = request.status_code
        log.save()

        if request.status_code == 404:
            return Response({'error': 'Invalid facebookId'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'error': request.text}, status=request.status_code)

class FbUserDelete(generics.GenericAPIView):
    def delete(self, request, *args, **kwargs):
        facebookId = self.kwargs.get('facebookId')
        if facebookId is None or facebookId is '':
            return Response({'error': 'facebookId field is required'}, status=status.HTTP_400_BAD_REQUEST)

        user = None
        try:
            user = FbUser.objects.get(facebookId=facebookId)
        except FbUser.DoesNotExist:
            return Response({'error': 'facebookId not found'}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        log = FbUserLog(action='deleted', facebookId=facebookId)
        log.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
