from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginView(TokenObtainPairView):
    ...


class AccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
