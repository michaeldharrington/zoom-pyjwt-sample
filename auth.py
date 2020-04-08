import jwt
from time import time
import secrets


def generateToken():
    token = jwt.encode(
        # Create a payload of the token containing API Key & exp time
        {"iss": secrets.API_KEY, "exp": time() + 5000},
        # Secret used to generate token signature
        secrets.API_SECRET,
        # Specify the hashing alg
        algorithm='HS256'
        # Converts token to utf-8
    ).decode('utf-8')

    return token
