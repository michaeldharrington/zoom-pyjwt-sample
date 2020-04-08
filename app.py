import requests
import json
import secrets
from auth import getHeaders


def getUsers():
    # Add a Zoom UserID, can be a userID or user's email
    # if blank, gets all users
    userId = ''

    # Create a GET request using requests library
    # Specify the endpoint: /v2/users/{userID}
    r = requests.get('https://api.zoom.us/v2/users/' +
                     userId, headers=getHeaders())

    # Print the requests status code
    print(r.status_code)
    # Print the response in JSON
    print(json.dumps(json.loads(r.text), indent=4))


getUsers()
