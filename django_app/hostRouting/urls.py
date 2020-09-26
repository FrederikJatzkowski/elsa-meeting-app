from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'(?P<year>.*)', views.index, name='index'),
    #re_path('', views.index, name='index'),
]