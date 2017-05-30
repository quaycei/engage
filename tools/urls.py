from django.conf.urls import url
from tools import views

urlpatterns = [
    url(r'^tools/$', views.tool_list, name='tool_list'),

 ]