from django.db import models
from uuid import uuid4


class CourseStatus(models.TextChoices):

    DEFAULT = "not started"
    IN_PROGRESS = "in progress"
    FINISHED = "finished"


class Course(models.Model):

    id = models.UUIDField(
        default=uuid4,
        primary_key=True,
        editable=False
    )
    name = models.CharField(
        max_length=100,
        unique=True
    )
    status = models.CharField(
        max_length=11,
        choices=CourseStatus.choices,
        default=CourseStatus.DEFAULT
    )
    start_date = models.DateField()
    end_date = models.DateField()

    instructor = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="courses",
        null=True
    )
