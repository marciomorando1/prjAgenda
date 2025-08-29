from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

class UserAccessMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(usuario=self.request.user)