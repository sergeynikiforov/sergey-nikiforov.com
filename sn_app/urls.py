from django.conf.urls import url
from sn_app import views

urlpatterns = [
    url(r'^$', views.landing, name = 'landing'),
    url(r'^resume$', views.resume, name = 'resume'),
    url(r'^about$', views.about, name = 'about'),
    url(r'^contact$', views.contact, name = 'contact')
]
