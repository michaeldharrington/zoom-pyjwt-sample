import jwt
from time import time
import requests
import json
import secrets

# Generate a JWT. Each request that is made uses a new token
encoded_jwt = jwt.encode(
    # Create a payload of the token containing API Key & exp time
    {"iss": secrets.API_KEY, "exp": time() + 5000},
    # Secret used to generate token signature
    secrets.API_SECRET,
    # Specify the hashing alg
    algorithm='HS256'
    # Converts token to utf-8
).decode('utf-8')

# Add a Zoom UserID, can be a userID or user's email
userId = ''

# Create headers for adding Bearer Token (JWT)
headers = {
    'authorization': f"Bearer {encoded_jwt}",
    'content-type': "application/json"
}

# Create a GET request using requests library
# Specify the endpoint: /v2/users/{userID}
r = requests.get('https://api.zoom.us/v2/users/' + userId, headers=headers)

# Print the requests status code
print(r.status_code)
# Print the response in JSON
print(r.json())
