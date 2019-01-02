from django.urls import path
from django.conf.urls import url

from frontend import views

urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^simple_upload/$', views.simple_upload, name='simple_upload'),
    url(r'^plant_more/$', views.plant_more, name='plant_more'),
    url(r'^plant_request/$',views.plant_request,name='plant_request'),
]
