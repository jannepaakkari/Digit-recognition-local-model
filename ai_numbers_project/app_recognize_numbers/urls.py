from django.urls import path, include
from . import views

# router = routers.DefaultRouter()

urlpatterns = [
    path('api/test/', views.TestView.as_view(), name="TestView"),
]
