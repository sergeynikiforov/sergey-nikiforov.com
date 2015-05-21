from django.conf.urls import url
from sn_app import views

urlpatterns = [
    url(r'^$', views.landing, name = 'landing')
]
