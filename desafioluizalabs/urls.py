from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt
from fbusers import views


urlpatterns = patterns('',
    # Examples:
    url(r'^person/$', csrf_exempt(views.FbUserList.as_view()), name='person'),
    url(r'^person/(?P<facebookId>\w+)/$', csrf_exempt(views.FbUserDelete.as_view()), name='person_delete'),
)
