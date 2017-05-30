from django.conf.urls import url
from onboard import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),

 ]