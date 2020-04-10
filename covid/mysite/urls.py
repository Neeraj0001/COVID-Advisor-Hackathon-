from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("home/",views.index,name='name'),
    path("meter/",views.meter,name='meter'),
    path("h_no/",views.h_no,name='h_no'),
    path("log_in/",views.login,name='login'),
    path("news/",views.news,name='news'),
    path("sign_in/",views.signup,name='signup'),
    path("form/",views.form,name='form'),
    path("fun/",views.fun,name='fun'),
    path("message/",views.messages,name='messages'),
]
