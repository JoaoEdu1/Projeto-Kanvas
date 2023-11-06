from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("accounts/", views.AccountView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
]
