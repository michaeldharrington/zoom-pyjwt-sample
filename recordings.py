import requests
import json
import secrets
from config import base
from auth import getHeaders


def getAccountRecordings():

    r = requests.get(base + '/accounts/me/recordings', headers=getHeaders())

    # Print the requests status code
    print(r.status_code)
    # Print the response in JSON
    print(json.dumps(json.loads(r.text), indent=4))


getAccountRecordings()
