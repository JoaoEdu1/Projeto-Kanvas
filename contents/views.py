from .models import Content
from courses.models import Course
from .serializers import ContentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissions import IsAdminUser, IsAdminOrOwner
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrStudentIsOwner
from rest_framework.exceptions import NotFound


class ContentView(generics.CreateAPIView):

    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "course_id"
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):

        course = get_object_or_404(Course, id=self.kwargs["course_id"])
        serializer.save(course=course)


class ContentDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        IsAuthenticated,
        IsAdminOrStudentIsOwner,
    ]

    serializer_class = ContentSerializer
    queryset = Content.objects.all()

    def get_object(self):
        course_id = self.kwargs["course_id"]
        content_id = self.kwargs["content_id"]

        try:
            Course.objects.get(id=course_id)
            obj_content = Content.objects.get(id=content_id)
        except Course.DoesNotExist:
            raise NotFound(
                {"detail": "course not found."},
            )
        except Content.DoesNotExist:
            raise NotFound(
                {"detail": "content not found."},
            )

        self.check_object_permissions(
            self.request,
            obj_content,
        )
        return obj_content
