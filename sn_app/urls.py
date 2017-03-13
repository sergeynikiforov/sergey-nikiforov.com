from django.conf.urls import url
from sn_app import views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^test[/]{0,1}$', views.test, name='test'),
    url(r'^resume[/]{0,1}$', views.resume, name='resume'),
    url(r'^contact[/]{0,1}$', views.contact, name='contact'),
    url(r'^photography[/]{0,1}$', views.photography, name='photography'),
    url(r'^photography/(?P<photoset_slug>[\w\-]+)[/]{0,1}$', views.photoset, name='photoset'),
    # start page for photo view - serve html
    url(r'^photography/(?P<photoset_slug>[\w\-]+)/photo/[\#a-zA-Z0-9_-]*$', views.photo_home, name='photo_home'),
    # get all photos for the album in json
    url(r'^photography/(?P<photoset_slug>[\w\-]+)/photo/api/photos/$', views.photoset_api, name='photoset_api'),
    # get photo info in json
    url(r'^photography/(?P<photoset_slug>[\w\-]+)/photo/api/photos/(?P<photoID>[a-zA-Z0-9_-]+)$', views.photo_api, name='photo_api')
]
