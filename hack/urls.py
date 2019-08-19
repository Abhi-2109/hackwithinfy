from django.urls import include, path
from django.conf.urls import url

from .views import home
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()





urlpatterns = [
    path('index', views.index),
    url(r'process', views.ProcessIt.as_view()),
    url(r'video', views.VideoPlay.as_view()),
    url(r'picture', views.PictureSee.as_view()),
]
