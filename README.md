# PyJWT with Zoom API

This sample app uses the [PyJWT](https://pyjwt.readthedocs.io/) and [Requests](https://requests.readthedocs.io/) libraries to request info on a single Zoom user. The user must be on the account associated with the API Key & Secret.

Use the Zoom [Users API Reference](https://marketplace.zoom.us/docs/api-reference/zoom-api/users/user) for full details on the endpoint.

## Install: 
```
pip3 install -r requirements.txt
```
Recommended: Install this in a [virtual environment](https://docs.python.org/3/library/venv.html). 

## Setup: 
### 1. Create JWT app on the Zoom Marketplace. 
Generate or retrieve an API Key & Secret for your Zoom account. Documentation: [Create a JWT App](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-jwt-app).

### 2. Add secrets
In `secrets.py`, add your API Key and Secret. 

*Never share these credentials publicly.* 

### 3. Specify a user
In `app.py`, specify the user you are requesting. This value can be a `userId` or the user's email.

## Usage: 
```
python app.py
```
Running the file prints a status code along with a JSON object representing the requested user. A new token is generated on each request. 