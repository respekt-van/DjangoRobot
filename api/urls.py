from django.urls import path
from .views import StatusView


app_name = "api"


# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('status/', StatusView.as_view()),
]