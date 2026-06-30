from rest_framework.permissions import BasePermission


class IsTeacher(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'teacher'


class IsLearner(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'learner'


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'admin'


class IsManager(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'manager'