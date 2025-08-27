import jwt
from django.conf import settings
from datetime import datetime, timedelta

def create_service_token():
    payload = {
        "iss": "internal-service",
        "exp": datetime.utcnow() + timedelta(minutes=30),
        "scope": "internal"
    }
    token = jwt.encode(payload, settings.SERVICE_JWT_SECRET, algorithm="HS256")
    return token

def verify_service_token(token):
    try:
        payload = jwt.decode(token, settings.SERVICE_JWT_SECRET, algorithms=["HS256"])
        return payload["scope"] == "internal"
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return False
