from .models import Content
from rest_framework import serializers


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        exclude = ["course"]

    def create(self, validated_data):
        return Content.objects.create(**validated_data)
