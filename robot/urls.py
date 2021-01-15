from django.urls import path
from .views import Robot


app_name = "robot"


# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('start/', Robot.as_view()),
]