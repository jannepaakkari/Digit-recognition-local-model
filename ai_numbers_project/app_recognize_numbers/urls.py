from django.urls import path, include
from . import views

# router = routers.DefaultRouter()

urlpatterns = [
    path('api/recognize/digit/',
         views.RecognizeDigit.as_view(), name="RecognizeDigit"),
]
