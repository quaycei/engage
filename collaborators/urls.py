from django.conf.urls import url
from collaborators import views

urlpatterns = [
    url(r'^update_collaborator/$', views.update_collaborator, name='update_collaborator'),
    url(r'^welcome/$', views.collaborator_welcome, name='collaborator_welcome'),

 ]