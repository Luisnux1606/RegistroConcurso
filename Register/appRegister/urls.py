from django.conf.urls import url,include
from django.urls import path,re_path
from .views import views


urlpatterns = [

    re_path(r'^registro/$', views.home, name="home"),
    re_path(r'^createPersona/$', views.createPersona, name="createPersona"),
    re_path(r'^gracias/$', views.gracias, name="gracias"),

]