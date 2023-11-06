from django.urls import path
from . import views


urlpatterns = [
    path("courses/", views.CourseView.as_view()),
    path("courses/<str:course_id>/", views.CourseDetailVIew.as_view()),
    path("courses/<str:course_id>/students/",
         views.StudentCourseView.as_view()),
]
