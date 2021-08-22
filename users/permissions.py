from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method == 'POST' or request.method == 'GET':
            return True

        return False
