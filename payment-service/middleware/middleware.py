from django.http import JsonResponse
from .utils.jwt import verify_service_token

class InterServiceAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/internal/"):  # protect only internal APIs
            auth_header = request.headers.get("Authorization")
            if not auth_header or not auth_header.startswith("Bearer "):
                return JsonResponse({"error": "Unauthorized"}, status=401)

            token = auth_header.split(" ")[1]
            if not verify_service_token(token):
                return JsonResponse({"error": "Invalid token"}, status=403)

        return self.get_response(request)
