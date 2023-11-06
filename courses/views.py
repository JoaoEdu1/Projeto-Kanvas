from .models import Course
from students_courses.models import StudentCourse
from accounts.models import Account
from students_courses.serializers import AddStudentCourseSerializer
from .serializers import CourseSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissions import IsAdminOrReadOnly, IsAdminOrOwner, IsAdminUser
from rest_framework import generics, serializers
from django.shortcuts import get_object_or_404


class CourseView(generics.ListCreateAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self) -> Course:
        user_admin = self.request.user.is_superuser
        course_id = self.request.user.id

        if not user_admin:
            return Course.objects.filter(students=course_id)

        return Course.objects.all()

    def perform_create(self, serializer):
        founded_instructor = "instructor"

        if not founded_instructor in serializer.validated_data:
            serializer.save()
        else:
            serializer.save(
                instructor=serializer.validated_data[founded_instructor])


class CourseDetailVIew(generics.RetrieveUpdateDestroyAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrOwner]


class StudentCourseView(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = AddStudentCourseSerializer
    lookup_url_kwarg = "course_id"
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
