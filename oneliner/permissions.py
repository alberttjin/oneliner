from rest_framework import permissions

class GetUserPermission(permissions.BasePermission):
    """
    Global permission check for getting a specific profile.
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj

class GetTaskPermission(permissions.BasePermission):
    """
    Global permission check for getting a specific profile.
    """

    def has_object_permission(self, request, view, obj):
        for profiles in obj.profile_set.all():
            if profiles.user == request.user:
                return True
        return False

class GetEventPermission(permissions.BasePermission):
    """
    Global permission check for getting events according to profile
    """

    def has_object_permission(self, request, view, obj):
        for profiles in obj.profile_set.all():
            if profiles.user == request.user:
                return True
        return False