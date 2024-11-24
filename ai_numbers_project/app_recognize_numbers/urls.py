from django.urls import path, include
from . import views

urlpatterns = [
    path('api/recognize/digit/',
         views.RecognizeDigit.as_view(), name="RecognizeDigit"),
]
