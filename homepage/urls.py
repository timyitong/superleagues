from django.conf.urls import patterns, include, url
from homepage import views

urlpatterns = patterns('',
    url(r'^$', 'homepage.views.home', name='home'),
)