from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):

        return request.user.is_superuser


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        return request.user.is_superuser


class IsAdminOrOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return (request.user.is_authenticated
                and obj == request.user
                and request.method == permissions.SAFE_METHODS
                or request.user.is_superuser)
