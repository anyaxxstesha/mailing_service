from django.core.exceptions import PermissionDenied


class UsersQuerySetMixin:
    view_permission = None

    def get_queryset(self):
        if self.request.user.has_perm(self.view_permission):
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user)


class ObjectOwnerPermissionMixin:
    permission_required = None

    def get_object(self):
        obj = super().get_object()
        if obj.user == self.request.user:
            return obj
        if self.request.user.has_perm(self.permission_required):
            return obj
        raise PermissionDenied


class UpdateObjectOwnerPermissionMixin(ObjectOwnerPermissionMixin):
    permission_form_class = None

    def get_form_class(self):
        if self.object.user == self.request.user:
            return super().get_form_class()
        if self.request.user.has_perm(self.permission_required):
            return self.permission_form_class

