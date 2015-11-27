from django.conf.urls import url
from sn_app import views

urlpatterns = [
    url(r'^$', views.landing, name = 'landing'),
    url(r'^resume$', views.resume, name = 'resume'),
    url(r'^about$', views.about, name = 'about'),
    url(r'^contact$', views.contact, name = 'contact'),
    url(r'^photography$', views.photography, name = 'photography'),
    url(r'^photography/(?P<photoset_slug>[\w\-]+)/$', views.photoset, name='photoset'),
    # start page for photo view - serve html
    url(r'^photography/(?P<photoset_slug>[\w\-]+)/photo/$', views.photo_home, name='photo_home'),
    # get all photos for the album in json
    url(r'^photography/(?P<photoset_slug>[\w\-]+)/photo/api/photos$', views.photoset_api, name='photoset_api'),
    # get photo info in json
    url(r'^photography/(?P<photoset_slug>[\w\-]+)/photo/api/photos/(?P<photoID>[\w\-]+)$', views.photo_api, name='photo_api'),
    #url(r'^photography/(?P<photoset_slug>[\w\-]+)/(?P<photoID>[\w\-]+)/$', views.photo, name='photo')
]
