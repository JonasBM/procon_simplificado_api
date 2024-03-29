from rest_framework import permissions


class IsAdminUserOrIsAuthenticatedReadOnly(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return bool(
            (request.method in permissions.SAFE_METHODS and (request.user and request.user.is_authenticated))
            or (request.user and request.user.is_staff)
        )


class IsAdminUserOrIsOwner(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return bool(obj == request.user or request.user.is_staff)


class IsAdminUserOrIsOwnerOrIsAuthenticatedReadOnly(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return bool(obj.owner == request.user or request.user.is_staff)


class IsOwnerOrIsAuthenticatedReadOnly(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return obj.owner == request.user
