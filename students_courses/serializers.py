from rest_framework import serializers
import accounts
from .models import StudentCourse
from courses.models import Course


class StudentCourseSerializer(serializers.ModelSerializer):

    student_username = serializers.CharField(
        max_length=150, source="student.username", read_only=True)

    student_email = serializers.CharField(
        max_length=150, source="student.email")

    class Meta:

        model = StudentCourse
        fields = ["id", "status", "student_id",
                  "student_email", "student_username"]


class AddStudentCourseSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True)
    name = serializers.CharField(max_length=100, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]

    def update(self, instance, validated_data):
        student_found = []
        student_not_found = []

        for student_course in validated_data["students_courses"]:
            student = student_course["student"]
            found = accounts.models.Account.objects.filter(
                email=student["email"]).first()

            if found:
                student_found.append(found)
            else:
                student_not_found.append(student["email"])

        if student_not_found:
            raise serializers.ValidationError({
                "detail": f"No active accounts was found: {', '.join(student_not_found)}."
            })

        instance.students.add(*student_found)

        instance.save()

        return instance
