from .models import Course
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class CourseSerializer(serializers.ModelSerializer):

    name = serializers.CharField(
        max_length=100,
        validators=[
            UniqueValidator(
                queryset=Course.objects.all(),
                message="course with this name already exists."
            )
        ])

    class Meta:

        model = Course
        fields = ["id", "name", "status", "start_date", "end_date",
                  "instructor", "contents", "students_courses"]
        extra_kwargs = {"contents": {"read_only": True},
                        "students_courses": {"read_only": True}}

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
