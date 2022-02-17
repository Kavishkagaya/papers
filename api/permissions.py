from rest_framework import permissions


class AllStaffAllcanEditANDuserReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if request.user.is_staff:
            return True

        if request.method in ['GET'] and request.user.is_authenticated :
            return True

        return False

    
