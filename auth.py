import os
import cachecontrol
import google.auth.transport.requests
import requests
from functools import wraps
from google.oauth2 import id_token

class AuthenticationFailedException(Exception):
    pass

def oidc_auth_required(request, email=None, audience=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kvargs):
            token = request.headers.get('idToken')
            session = requests.session()
            cached_session = cachecontrol.CacheControl(session)
            transport_request = google.auth.transport.requests.Request(session=cached_session)

            decoded_token = id_token.verify_oauth2_token(token, transport_request)
            if decoded_token['iss'] != 'accounts.google.com':
                raise AuthenticationFailedException()

            if email and decoded_token['email'] != email:
                raise AuthenticationFailedException()

            return f(*args, **kvargs)
        return wrapper
    return decorator