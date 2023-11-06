from rest_framework import permissions


class IsAdminOrStudentIsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        return (
            request.method in permissions.SAFE_METHODS
            and request.user in obj.course.students.all()
        )
