from django.urls import path
from . import views


urlpatterns = [
    path("courses/<str:course_id>/contents/",
         views.ContentView.as_view()),
    path("courses/<str:course_id>/contents/<str:content_id>/",
         views.ContentDetailView.as_view())
]
