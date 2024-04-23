from .import views
from django.urls import path

urlpatterns = [
    path("", views.aboutView, name="about"),
]