from . import views
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
]