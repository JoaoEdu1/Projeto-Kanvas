from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account


class AccountSerializer(serializers.ModelSerializer):

    email = serializers.CharField(max_length=100, validators=[
        UniqueValidator(
            queryset=Account.objects.all(),
            message="user with this email already exists.")
    ])

    class Meta:
        model = Account
        fields = ["id", "username", "password", "email", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> Account:
        if validated_data["is_superuser"]:
            return Account.objects.create_superuser(**validated_data)

        return Account.objects.create_user(**validated_data)
