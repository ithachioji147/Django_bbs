from django.shortcuts import redirect
from django.conf import settings

# アクセス制限
class RestrictAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in settings.ALLOWED_PATHS:
            return redirect('main:login')

        response = self.get_response(request)
        return response
