from django.urls import path
from . import views


urlpatterns = [
    path('', views.start, name='default'),
    path('user_defined', views.defined, name='defined'),
    path('success', views.result, name="result"),
    path('logs', views.entrylogs, name="logs")
]
