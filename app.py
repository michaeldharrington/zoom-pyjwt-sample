import requests
import json
import secrets
from auth import generateToken

# Add a Zoom UserID, can be a userID or user's email
# if blank, gets all users
userId = ''

# Create headers for adding Bearer Token (JWT)
headers = {
    'authorization': f"Bearer {generateToken()}",
    'content-type': "application/json"
}

# Create a GET request using requests library
# Specify the endpoint: /v2/users/{userID}
r = requests.get('https://api.zoom.us/v2/users/' + userId, headers=headers)

# Print the requests status code
print(r.status_code)
# Print the response in JSON
print(json.dumps(json.loads(r.text), indent=4))
